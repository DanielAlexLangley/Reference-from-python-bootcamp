
# https://gist.github.com/angelabauer/4e303378383f2b847361740ce6e59997
# https://gist.github.com/angelabauer/3def76077443db8d184fb741fa6141e3
# https://gist.github.com/angelabauer/a61522818d3688730ddd8170f42e0635
# https://gist.github.com/angelabauer/03d622f7ad854602a019ac117ad4b83d
# https://gist.github.com/angelabauer/de2f3faa28586ca970032f9249f2b310

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
