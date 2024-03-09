from flask import Flask, request, jsonify, render_template, Response
from library import Library

app = Flask(__name__, template_folder='templates')
library = Library()

@app.route('/')
@app.route('/index.html')
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
    message = library.add_books(title, author, quantity)
    return jsonify({"message": message})

@app.route('/borrow_book_form')
def borrow_book_form():
    return render_template('borrow_book_form.html')
    
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    data = request.get_json()
    title = data.get('title')
    message = library.borrow_books(title)
    return jsonify({"message": message})

@app.route('/return_book_form')
def return_book_form():
    return render_template('return_book_form.html')

@app.route('/return_book', methods=['POST'])
def return_book():
    data = request.get_json()
    title = data.get('title')
    message = library.return_books(title)
    return jsonify({"message": message})

@app.route('/display_book', methods=['GET'])
def display_book():
    cursor = library.display_books2()
    if cursor:
        def generate():
            yield '<ul>'
            for row in cursor:
                title, author, quantity, available_quantity = row
                yield f'<h2>{title} by {author} - Available: {available_quantity}/{quantity}</h2>'
            yield '</ul>'
        return Response(generate(), content_type='text/html')
    else:
        return "Error loading books", 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')