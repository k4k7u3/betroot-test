from flask import Flask, render_template, url_for, request
from flask import render_template, flash, redirect
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from apiclient.discovery import build


from app.forms import LoginForm, RegisterForm
from app.user import User


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
    cursor.execute(f'SELECT * FROM rezerv_users where rezerv_users.id = (%s)', (id,))
    person = cursor.fetchone()
    cursor.close()
    user = User(person[0], person[1], person[2], person[4])
    user.is_authenticated = True
    return user


@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def main():
    return render_template("home.html", title="Home")


@app.route('/products', methods=["GET", "POST"])
def products():
    return render_template("products.html", title="Products")


@app.route('/login', methods=["GET", "POST"])
def login():
    method = request.method
    form = LoginForm()
    if form.validate_on_submit():
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                      password='qwe123')
        cursor = connection.cursor()
        cursor.execute(f'SELECT id, name, password_hash, admin FROM rezerv_users where rezerv_users.name = (%s)', (form.username.data,))
        user_data = cursor.fetchone()
        if user_data is None:
            cursor.close()
            flash('Неверное имя')
            return redirect(url_for('login'))
        cursor.close()
        user = User(user_data[0], user_data[1], user_data[2], user_data[3])
        if not user.check_password(form.password.data):
            flash('Неверный пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(f'/home')
    return render_template("login.html", title="Login", form=form)


@app.route('/logout', methods=["GET", "POST"])
def logout():
    method = request.method
    logout_user()
    return render_template("home.html", title="Home")


@app.route('/register', methods=["GET", "POST"])
def register():
    method = request.method
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        psw_hash = generate_password_hash(reg_form.password.data)
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres',
                                      password='qwe123')
        cursor = connection.cursor()
        cursor.execute("Insert into rezerv_users (name, password_hash, email, admin) values (%s, %s, %s, %s)",
                       (reg_form.username.data, psw_hash, reg_form.email.data, "True"))
        connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=reg_form)


@app.route('/contacts', methods=["GET", "POST"])
def contacts():
    method = request.method
    return render_template("contacts.html", title="PIU")


@app.route('/pyp', methods=["GET", "POST"])
def pyp():
    method = request.method
    return render_template("about_pyp.html", title="PYP")


@app.route('/ppy_pt', methods=["GET", "POST"])
def ppy_pt():
    method = request.method
    return render_template("about_ppypt.html", title="PPY_PT")


@app.route('/ppkp', methods=["GET", "POST"])
def ppkp():
    method = request.method
    return render_template("about_ppkp.html", title="PPKP")


@app.route('/brvu', methods=["GET", "POST"])
def brvu():
    method = request.method
    return render_template("about_brvu.html", title="BRVU")


@app.route('/bdu', methods=["GET", "POST"])
def bdu():
    method = request.method
    return render_template("about_bdu.html", title="BDU")


@app.route('/brit', methods=["GET", "POST"])
def brit():
    method = request.method
    return render_template("about_brit.html", title="BRIT")


@app.route('/dvp', methods=["GET", "POST"])
def dvp():
    method = request.method
    return render_template("about_dvp.html", title="DVP")


@app.route('/piu', methods=["GET", "POST"])
def piu():
    method = request.method
    return render_template("about_piu.html", title="PIU")


@app.route('/OmegaSystem', methods=["GET", "POST"])
def OmegaSystem():
    method = request.method
    return render_template("OmegaSystem.html")


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5554)
