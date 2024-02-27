from flask import Flask, request, jsonify, render_template
from library import Library

app = Flask(__name__, template_folder='template')
library = Library()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book_form')
def add_book_form():
    return render_template('add_book_form.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    quantity = data.get('quantity', 1)
    library.add_books(title, author, quantity)
    return jsonify({"message": "Book added successfully"})

@app.route('/borrow_book_form')
def borrow_book_form():
    return render_template('borrow_book_form.html')
    
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    data = request.get_json()
    title = data.get('title')
    library.borrow_books(title)
    return jsonify({"message": "Book borrowed successfully"})

@app.route('/return_book_form')
def return_book_form():
    return render_template('return_book_form.html')

@app.route('/return_book', methods=['POST'])
def return_book():
    data = request.get_json()
    title = data.get('title')
    library.return_books(title)
    return jsonify({"message": "Book returned successfully"})

@app.route('/display_book', methods=['GET'])
def display_book():
    library.display_books()
    return jsonify({"message": "All books displayed"})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')