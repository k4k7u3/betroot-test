from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import psycopg2


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign in")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        connection = psycopg2.connect(host='localhost',
                                      database='postgres',
                                      port=5432,
                                      user='postgres',
                                      password='qwe123')

        cursor = connection.cursor()
        cursor.execute("SELECT name FROM users where name = (%s)", (username.data,))
        name_validation = cursor.fetchone()
        cursor.close()
        if name_validation:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        connection = psycopg2.connect(host='localhost',
                                      database='postgres',
                                      port=5432,
                                      user='postgres',
                                      password='qwe123')

        cursor = connection.cursor()
        cursor.execute("SELECT name FROM users where name = (%s)", (email.data,))
        email_validation = cursor.fetchone()
        cursor.close()
        if email_validation:
            raise ValidationError('Please use a different email address.')


class SearchForm(FlaskForm):
    ISBN = StringField("ISBN:", validators=[DataRequired()])
    submit = SubmitField("Search")


class AddBookForm(FlaskForm):
    review = TextAreaField("Review:")
    submit = SubmitField("Add")


class ChangeInfo(FlaskForm):
    title = StringField("Title:")
    author = StringField("Author:")
    description = TextAreaField("Description:")
    review = TextAreaField("Review:")
    submit = SubmitField("Change")
    submit_delete = SubmitField("Delete book")
