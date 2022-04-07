
from flask import Flask, render_template
from bootstrap_blog_post import Post
import requests
app = Flask(__name__)

posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be").json()
post_objects = []
# The for loop immediately below this will create an object for each "post"...
# ...and the list above will hold each of those objects in order, so that they can be referenced by their index.
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    post_objects.append(post_obj)


@app.route("/")
@app.route("/index.html")
def home_page():
    return render_template("index.html", posts=post_objects)


@app.route("/about.html")
def about_page():
    return render_template("about.html")


@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    print(index)
    requested_post = None
    for blog_post in post_objects:
        print(blog_post.id)
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("/templates/post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
