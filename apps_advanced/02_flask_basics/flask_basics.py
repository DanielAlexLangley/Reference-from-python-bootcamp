
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


# Flask accepts HTML in the return:
@app.route("/testing")
def testing():
    # Anything you can do with inline styling with CSS,
    # or changing code to any sort of HTML tag, you can do in this return.
    # What if you wanted to return more than one HTML element?
    return '<h1 style="text-align: center">Testing!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/3o6ZsZwsU65E0qcok8/giphy.gif" width=200>'


# Instead of adding HTML directly into the return, it is better to use functions:
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper
def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#debug-mode
# See Python bootcamp lesson 453 for more info on debugger mode, and accessing the console from the browser.
if __name__ == "__main__":
    app.run(debug=True)
