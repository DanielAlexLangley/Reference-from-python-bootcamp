
# Professor's solution code:
# https://gist.github.com/TheMuellenator/7c6a08a3df3b94a28d1a867628481910

from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    data_blogs = response.json()
    return render_template("index.html", posts=data_blogs)


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    data_blogs = response.json()
    data_blog = data_blogs[int(num)]
    print(data_blog)
    return render_template('post.html', post=data_blog)


if __name__ == "__main__":
    app.run(debug=True)
