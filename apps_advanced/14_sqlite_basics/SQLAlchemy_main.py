
# https://gist.github.com/angelabauer/d7af893cdd72311d674d709421fa389d

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# CREATE RECORD
new_book = Book(id=2, title="Harry Potter2", author="J. K. Rowling", rating=9.3)
# NOTE: When creating new records, the primary key fields is optional. you can also write:
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# the id field will be auto-generated.
db.session.add(new_book)
db.session.commit()

# Read All Records
# all_books = db.session.query(Book).all()
#
# Read A Particular Record By Query
# book = Book.query.filter_by(title="Harry Potter").first()
#
# Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
#
# Update A Record By PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
#
# Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
#
# You can also delete by querying for a particular value e.g. by title or one of the other properties.
