
# https://gist.github.com/angelabauer/045264ca6ad168b986f6687ee1368078

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


# Notice that the method's parameter accepts a dictionary,
# so you can have multiple methods targeted by one route. e.g. @app.route("/contact", methods=["GET", "POST"]
@app.route('/login', methods=["POST"])
def login():
    if request.method == 'POST':
        # return render_template('login.html', username=request.form['username'], password=request.form['password'])
        name = request.form['username']
        password = request.form['password']
        return f"<h1>Name: {name}, Password: {password} </h1>"


if __name__ == "__main__":
    app.run(debug=True)
