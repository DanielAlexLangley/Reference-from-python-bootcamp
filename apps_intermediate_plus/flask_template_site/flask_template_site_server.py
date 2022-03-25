
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# In the browser press f12 for developer tools, then type:
# document.body.contentEditable=true
# In the console.
# This will let us edit the HTML directly in the browser.
# Can use select tool to select an element, then backspace to delete it.
# To save you have to save the page as an HTML file, then replace the old version of the file with the new version.
