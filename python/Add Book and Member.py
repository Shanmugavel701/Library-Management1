# ...

# Helper function to find a book by its ID
def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        quantity = int(request.form['quantity'])

        book_id = len(books) + 1  # Generating a simple ID for the new book
        book = {'id': book_id, 'name': name, 'author': author, 'quantity': quantity}
        books.append(book)

        flash('Book added successfully', 'success')
        return redirect(url_for('view_books'))

    return render_template('add_book.html')

@app.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    book = find_book(book_id)
    if not book:
        flash('Book not found', 'danger')
        return redirect(url_for('view_books'))

    if request.method == 'POST':
        book['name'] = request.form['name']
        book['author'] = request.form['author']
        book['quantity'] = int(request.form['quantity'])

        flash('Book updated successfully', 'success')
        return redirect(url_for('view_books'))

    return render_template('edit_book.html', book=book)

@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = find_book(book_id)
    if book:
        books.remove(book)
        flash('Book deleted successfully', 'success')

    return redirect(url_for('view_books'))

# Similar CRUD operations can be implemented for members
# Add, Edit, Delete Member views and functions

if __name__ == "__main__":
    app.run(debug=True)
