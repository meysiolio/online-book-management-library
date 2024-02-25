from flask import Flask, request, jsonify
from library import Library

app = Flask(__name__)
library = Library()

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    quantity = data.get('quantity', 1)
    library.add_books(title, author, quantity)
    return jsonify({"message": "Book added successfully"})

if __name__ == '__main__':
    app.run(debug=True)