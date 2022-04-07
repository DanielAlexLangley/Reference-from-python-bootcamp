
# https://genderize.io/
# https://agify.io/

from flask import Flask, render_template
import datetime
import requests
import random
app = Flask(__name__)


@app.route("/")
def homepage():
    random_number = random.randint(1, 10)
    now = datetime.datetime.now().year
    name = "Daniel"
    # Can add as many keyword arguments as I need: each needs a name and value.
    return render_template('index.html', num=random_number, year=now, my_name=name)


@app.route("/guess/<string:name>")
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    data_agify = response.json()
    response = requests.get(f"https://api.genderize.io?name={name}")
    data_genderize = response.json()
    return render_template('guess.html', guess_name=name.capitalize(),
                           guess_gender=data_genderize["gender"],
                           guess_age=data_agify["age"])


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    data_blogs = response.json()
    return render_template('blog.html', posts=data_blogs)


if __name__ == "__main__":
    app.run(debug=True)

# Jinja allows us to put code between {{ }},
# and that code will be run as Python code,
# even if that code is in an HTML file.
# This is why Jinja is known as a templating langauge.
# It means we can have HTML which acts as a template,
# and only the parts which we specify will be evaluated
# as Python code then inserted into the template.

# But what if we wanted to create multiline
# Python statement in the HTML file,
# like an if statement, or a for loop:
# (see blog example above).
# What about an if statement?
# Similar answer, see documentation of jinja,
# (and also see blog example).

# Also URL building.
# See index.html for example.
