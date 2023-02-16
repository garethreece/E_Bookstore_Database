# This is the program for commnicating with the database. Please run bookstore_app.py to allow users to view and edit the database

##########################################
### RUN BOOKSTORE_APP.PY NOT THIS FILE ###
##########################################

### IMPORTS ###

# import the sqlite3 module
import sqlite3
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()  # Get a cursor object
# Carried out a code checker to see if there was any vunerabilities with injection attacks
# https://snyk.io/code-checker/ Synk online checker couldn't find any injection security issues


### DEFINE FUNCTIONS###

# For most of the funtions the SQL statements used are save in global variables that return the relevant text.

def create_tables():
    #create a table called books with id, title, author, and qty as column headers
    cursor.execute(create_books_table)
    db.commit()

def add_initial_data():
    # insert the initial book data into the db unless it already exists
    i = 0
    # Used a while loop to input the global list variable initial_database_values() one at a time
    while i < len(initial_database_values):
        # SQL statement to insert or replace the data for each book as defined by the task
        cursor.execute('''
        INSERT OR REPLACE INTO books (id, title, author, qty)
        VALUES (?,?,?,?)
        ''', initial_database_values[i])
        # save changes by commiting to db
        db.commit()
        i += 1

# function to add a book into the database using title, author, and quantity defined by user info in bookstore_app.py
def add_book(title, author, qty):
    cursor.execute(insert_book, (title, author, qty))
    db.commit()

# function to view all books in the database and return info to user
def view_all_books():
    return cursor.execute(view_books).fetchall()

# function to search all books by title in the database and return info to user
def search_books(title):
    return cursor.execute(find_book, (title,)).fetchall()

# function to search all books by id  in the database and return info to user
def search_id(id_of_book):
    return cursor.execute(find_id, (id_of_book,)).fetchall()

# function to delete a book dependent on the id data (primary key) received
def delete_row(id_of_book):
    cursor.execute(delete_book, (id_of_book,))
    db.commit()

# function to update title of book based on the id data (primary key) received
def update_title(title, id_of_book):
    cursor.execute(update_title_db, (title, id_of_book))

# function to update author of book based on the id data (primary key) received
def update_author(author, id_of_book):
    cursor.execute(update_author_db, (author, id_of_book))

# function to update quantity of books based on the id data (primary key) received
def update_quantity(qty, id_of_book):
    cursor.execute(update_quantity_db, (qty, id_of_book))

# function to commit / save any changes to the database
def commit_changes():
    db.commit()

# function to roll back any changes made to the database (back to the last commit / save)
def rollback_changes():
    db.rollback()

# close the connection with the ebookstore 
# database
def close_connection():
    db.close()


### DEFINE GLOBAL VARIABLES ###

# SQL statement that creates a table if it doesn't exist. The table includes:
#  - id (int primary key), title (text), author (text), and quantity (integer) 
create_books_table = '''CREATE TABLE IF NOT EXISTS books 
(id INTEGER PRIMARY KEY NOT NULL,
Title TEXT,
Author TEXT,
Qty INTEGER);'''

# SQL statement to insert a new book by title, author, qty. 
# The id is the primary key that is automatically assigned to all new books
insert_book = '''INSERT INTO books 
(
    Title,
    Author,
    Qty
) VALUES (?,?,?);'''

# SQL statement to get all the database info from books
view_books = ''' SELECT * FROM books;'''

# SQL statement to find all the books with a term 'like' and return all column info for those books to the user
find_book = '''SELECT * FROM books WHERE title LIKE '%'||?||'%';'''

#SQL statement to find a book based on a specific ID number
find_id = '''SELECT * FROM books WHERE id = ?;'''

#SQL statement to delete a book based on a specific ID number
delete_book = '''DELETE FROM books where id = ?;'''

# Grouped these SQL statement together as they were similar 
# To update a book (title, author, or quantity) based on a specific ID number
update_title_db = '''UPDATE books SET title = ? WHERE id = ?;'''
update_author_db = '''UPDATE books SET author = ? WHERE id = ?;'''
update_quantity_db = '''UPDATE books SET qty = ? WHERE id = ?;'''

# Initial database information that is required to create the database and table, as dtated in the task PDF
initial_database_values = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion the Witch and the Wadrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]
