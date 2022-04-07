
# https://gist.github.com/angelabauer/97e23a7e6a044413ec3ed76456fd1c2e
# https://gist.github.com/angelabauer/bcb90f5060fe7204814da3249b069b7b
# https://gist.github.com/angelabauer/4db9f611e8b11a86021dc2eb6cdc61e7
# https://gist.github.com/angelabauer/6e9dec2b75b3d6b4b5f2feed011a0d13

from flask import Flask, render_template, request
import requests
import smtplib
import os

env_var_mailtrap_password = os.environ.get("ENV_VAR_MAILTRAP_PASSWORD")
env_var_mailtrap_username = os.environ.get("ENV_VAR_MAILTRAP_USERNAME")

message = f"""\
Subject: Hi Mailtrap
To: receiver
From: sender

This is a test e-mail message."""


posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be").json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        sender = f"{data['name']} {data['email']}"
        receiver = "A Test User <to@example.com>"
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login(env_var_mailtrap_username, env_var_mailtrap_password)
            server.sendmail(sender, receiver, message)
        # print(data["name"])
        # print(data["email"])
        # print(data["phone"])
        # print(data["message"])
        return render_template("contact.html", sent=True)
    return render_template("contact.html", sent=False)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         message = request.form['message']
#         print(name)
#         print(email)
#         print(phone)
#         print(message)
#         return "<h1>Successfully sent your message!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
