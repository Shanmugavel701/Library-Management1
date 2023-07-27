# ...

@app.route('/books/<int:book_id>/issue/<int:member_id>', methods=['POST'])
def issue_book(book_id, member_id):
    book = find_book(book_id)
    if not book or book['quantity'] <= 0:
        flash('Book not available for issue', 'danger')
    else:
        member = next((member for member in members if member['id'] == member_id), None)
        if not member:
            flash('Member not found', 'danger')
        else:
            book['quantity'] -= 1
            transaction = {'book_id': book_id, 'member_id': member_id, 'type': 'issue'}
            transactions.append(transaction)
            flash('Book issued successfully', 'success')

    return redirect(url_for('view_books'))

@app.route('/books/<int:book_id>/return/<int:member_id>', methods=['POST'])
def return_book(book_id, member_id):
    book = find_book(book_id)
    if not book:
        flash('Book not found', 'danger')
    else:
        member = next((member for member in members if member['id'] == member_id), None)
        if not member:
            flash('Member not found', 'danger')
        else:
            book['quantity'] += 1
            transaction = {'book_id': book_id, 'member_id': member_id, 'type': 'return'}
            transactions.append(transaction)

            # Calculate book fee (if any)
            if member['outstanding_debt'] <= 500:
                book_fee = 50  # Assuming a flat fee of Rs. 50 per book return
                member['outstanding_debt'] += book_fee

            flash('Book returned successfully', 'success')

    return redirect(url_for('view_books'))

# ...

if __name__ == "__main__":
    app.run(debug=True)
