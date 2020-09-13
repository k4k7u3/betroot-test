from flask import Flask, render_template, url_for, request
from flask import render_template, flash, redirect
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

import requests
import sys
import json
import datetime

from app.forms import LoginForm, RegistrationForm, SearchForm, AddBookForm, ChangeInfo
from app.user import User

isbn = ""
api_key = "#######"
articles = None

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
login = LoginManager(app)
login.login_view = 'login'



@login.user_loader
def load_user(id):
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                  password='qwe123')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM users where users.id = (%s)', (id,))
    person = cursor.fetchone()
    cursor.close()
    user = User(person[0], person[1], person[2])
    user.is_authenticated = True
    return user


@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def main():
    return render_template("home.html", title="BookGeek")


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html", title="BookGeek")


@app.route('/about_romance', methods=["GET", "POST"])
def about_romance():
    return render_template("about_romance.html", title="BookGeek")


@app.route('/user/<string:name>')
def user(name):
    method = request.method
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                  password='qwe123')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.books where user_name = %s", (current_user.name,))
    user_books = cursor.fetchall()
    cursor.close()
    return render_template("user_page.html", posts=user_books)


@app.route('/user/<string:name>/<int:id>', methods=["GET", "POST"])
def book_change(name, id):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                  password='qwe123')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.books where id = %s and  user_name = %s", (id, name))
    change_book = cursor.fetchone()
    change_form = ChangeInfo(title=change_book[2], author=change_book[3], description=change_book[5], review=change_book[6])
    if change_form.validate_on_submit():
        if change_form.submit.data:
            if change_form.title.data == "":
                flash('Title cannot be empty')
                return redirect(f"/user/{name}/{id}")
            elif change_form.author.data == "":
                flash('Author cannot be empty')
                return redirect(f"/user/{name}/{id}")
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                          password='qwe123')
            cursor = connection.cursor()
            cursor.execute("UPDATE public.books SET title = %s, authors = %s, description = %s, review = %s where id = %s and user_name = %s", (change_form.title.data, change_form.author.data, change_form.description.data, change_form.review.data, id, name))
            connection.commit()
            cursor.close()
            return redirect(f'/user/{name}')
        elif change_form.submit_delete.data:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                          password='qwe123')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.books where user_name = %s and id = %s", (name, id))
            connection.commit()
            cursor.close()
            return redirect(f'/user/{name}')
    return render_template("change_book.html", form=change_form)


@app.route('/add', methods=["GET", "POST"])
def add_book():
    global articles
    method = request.method
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    book_form = AddBookForm(request.form)
    if book_form.validate_on_submit():
        data_time = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                      password='qwe123')
        cursor = connection.cursor()
        cursor.execute("Insert into books (user_name, title, authors, published_date, description, review, add_date) values (%s, %s, %s, %s, %s, %s, %s)",
                       (current_user.name, articles['items'][0]['volumeInfo']['title'], articles['items'][0]['volumeInfo']['authors'], articles['items'][0]['volumeInfo']['publishedDate'], articles['items'][0]['volumeInfo']['description'], book_form.review.data, data_time))
        connection.commit()
        cursor.close()
        return redirect(f'/user/{current_user.name}')
    return render_template("add.html", articles=articles, form=book_form)


@app.route('/result', methods=["GET", "POST"])
def result():
    global isbn, articles
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    params = {"q": f"isbn:{isbn}", "key": f"{api_key}"}
    resp = requests.get("https://www.googleapis.com/books/v1/volumes", params=params)
    articles = resp.json()
    return render_template("result.html", articles=articles)


@app.route('/search', methods=["GET", "POST"])
def search():
    global isbn
    method = request.method
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    search_form = SearchForm()
    if search_form.validate_on_submit():
        if search_form.ISBN.data.isdigit() == False:
            flash('ISBN code must consist of numbers')
            return redirect(url_for('search'))
        elif len(search_form.ISBN.data) != 13:
            flash('ISBN code must consist of 13 numbers')
            return redirect(url_for('search'))
        isbn = search_form.ISBN.data
        return redirect(url_for('result'))
    return render_template("search.html", form=search_form)


@app.route('/logout', methods=["GET", "POST"])
def logout():
    method = request.method
    logout_user()
    if method == "GET":
        return render_template("base.html", title="BookGeek")
    else:
        return redirect(url_for('home'))


@app.route('/login', methods=["GET", "POST"])
def login():
    method = request.method
    if current_user.is_authenticated:
        if method == "GET":
            return render_template("base.html", title="BookGeek")
        else:
            return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                      password='qwe123')
        cursor = connection.cursor()
        cursor.execute(f'SELECT id, name, password_hash FROM users where users.name = (%s)', (form.username.data,))
        user_data = cursor.fetchone()
        if user_data is None:
            cursor.close()
            flash('Invalid username')
            return redirect(url_for('login'))
        cursor.close()
        user = User(user_data[0], user_data[1], user_data[2])
        if not user.check_password(form.password.data):
            flash('Invalid password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(f'/user/{user.name}')
    return render_template("login.html", title="Sign In", form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        psw_hash = generate_password_hash(reg_form.password.data)
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                      password='qwe123')
        cursor = connection.cursor()
        cursor.execute("Insert into users (name, password_hash, email) values (%s, %s, %s)", (reg_form.username.data, psw_hash, reg_form.email.data))
        connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=reg_form)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5555)
