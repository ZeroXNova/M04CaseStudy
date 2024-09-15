from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    publisher = db.Column(db.String(80), unique=False, nullable=False)

def __repr(self):
    return f"{self.book_name} - {self.description} - {self.author} - {self.publisher}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/book')
def get_book():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)
    return {"book_name": output}

@app.route('/book/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}