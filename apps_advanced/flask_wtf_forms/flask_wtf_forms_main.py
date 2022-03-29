
# https://gist.github.com/TheMuellenator/29acd670326c6313bc2b8f7e66fd441f
# https://gist.github.com/angelabauer/162f56578b9193090963a0691c826790
# https://gist.github.com/angelabauer/e5b1a26a79888f67b490c1f53ed2496c
# https://gist.github.com/angelabauer/20ba20298ee26c957f36176291de9d69
# https://gist.github.com/angelabauer/aa7a7516bf02b1f0f1769dadaf4e6cf4
# https://gist.github.com/angelabauer/9842d06ca3b5c1c6668bef0f7f0601cb

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
import os


class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email(check_deliverability=True)],
        render_kw={'style': 'width: 30ch'}
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(min=8)],
        render_kw={'style': 'width: 40ch'}
    )
    submit = SubmitField(label='Log In', render_kw={'btn-primary': 'True'})


app = Flask(__name__)
app.secret_key = os.environ.get("ENV_VAR_WTF_CSRF_SECRET_KEY")
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
