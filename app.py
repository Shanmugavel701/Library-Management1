from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# Sample data for simplicity. You can replace this with a database later.
books = [
    {'id': 1, 'name': 'Book 1', 'author': 'Author 1', 'quantity': 5},
    {'id': 2, 'name': 'Book 2', 'author': 'Author 2', 'quantity': 3},
    # Add more sample books here
]

members = [
    {'id': 1, 'name': 'Member 1', 'outstanding_debt': 0},
    {'id': 2, 'name': 'Member 2', 'outstanding_debt': 100},
    # Add more sample members here
]

transactions = []  # List to store book issue and return transactions

# Routes and View Functions will go here

if __name__ == "__main__":
    app.run(debug=True)
