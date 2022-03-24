
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules
# "Parsing the URL" is getting the URL the user typed in.
@app.route("/username/<name>/1")  # This will turn whatever is inside <name> into a variable "name" for us to use.
def greet(name):
    return f"Hello {name}!"
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules
# A "converter" will convert the URL into any datatype that you specify.
# By default, converts to a string.
# You can also have multiple variables, like:
# @app.route("/username/<name>/<int:number>")


@app.route("/bye")
def say_bye():
    return "Bye!"


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#debug-mode
# See Python bootcamp lesson 453 for more info on debugger mode, and accessing the console from the browser.
if __name__ == "__main__":
    app.run(debug=True)
