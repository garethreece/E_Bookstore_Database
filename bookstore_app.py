# This is the main program for the bookshop database and needs to be run to enable it to work!
# This is for the user code to run the bookstore application
# Carried out a code checker to see if there were any vulnerabilities with injection attacks
# https://snyk.io/code-checker/ Synk online checker couldn't find any injection security issues

#####################
### RUN THIS FILE ###
#####################

### IMPORT MODULES ###
# This file (bookstore_app.py) is for the users to interface with that includes the menu system
# I created another file (bookshop.py) to interface with the e-bookstore database and imported it to this file.
import bookshop
# imported tabulate to make the results from the bookshop database look neater in python
from tabulate import tabulate

# This menu function reacts to inputs from the user for each menu item. 
def menu():
# While loop to keep the program running whilst the response is not '0'
    while (menu_input := input(menu_text)) != '0':
        if menu_input == '1':
            enter_book()
        elif menu_input == '2':
            update_book()
        elif menu_input == '3':
            delete_book()
        elif menu_input == '4':
            search_book()
        elif menu_input == '5':
            view_all_books()
        else:
            invalid_input()

# From main menu 1 - This function adds a new book to the database. 
# Character limitations for inputs have been put in place to stop any over complicated data
def enter_book():
    # get title info from title() function
    title_add = title()
    # get author info from author() function
    author_add = author()
    # get quantity info from the quantity() function
    qty_add = quantity()
    # Once the relevant data is captured for a new book, 
    # it will send the information to the bookshop.py file - add_book() function
    bookshop.add_book(title_add, author_add, qty_add)

# Main menu item number 2 - Update a book in the database
def update_book():
    # Made the user identify the book by its primary key... This way each book is unique and there is no ambiguity
    # The user can search or view all books to locate the id from the main menu.
    id_of_book = input("What is the ID number of the book: ")
    # This will send the information to the bookshop.py file - search_id () function to locate the book.
    book = bookshop.search_id(id_of_book)
    # While loop to check the data returned from bookshop.py is valid
    while True:
        # If no data is returned, then the program will respond with 'not found', break the loop,
        # and return to the main menu.
        if book == []:
            print("No book found with that id, returning to main menu!")
            break
        # If data is returned from the database it will assume it has found a book and process the request
        # Program confirms the data, shows all the info to the user and asks for a last check that they want to update
        print("\n\033[1;4mAre you sure you want to update this book?\033[0m")
        # Tabulate import is used to display the information in a pretty format with headers
        print(tabulate(book, headers=["Book ID","Title", "Author", "Quantity"], tablefmt="pretty"))
        check = input("Yes(Y) / No (N): ").upper()
        # If yes will go to the update_options menu to ask what needs updating
        if check == 'Y' or check == 'YES':
            update_options(id_of_book)
            break
        # If anything else is inputted by the user (apart from y or yes), then it will return to the main menu
        else:
            print("Book has not been updated, returning to main menu.")
            break

# Function to update the book - I separated the update into Title, Author, Quantity
# This can be saved at the end of the update (or you can exit without saving).
def update_options(id_of_book):
    # Loop to update different fields for the chosen book, and show what is being changed.
    while True:
        # I need to get the latest data for the book being updated for each loop,
        # this shows the changes being made in real time
        book = bookshop.search_id(id_of_book)
        # Shows the book info at the top of each loop and menu option
        print(tabulate(book, headers=["Book ID","Title", "Author", "Quantity"], tablefmt="pretty"))
        # Menu text is shown in update_text function and returned here
        menu_input = input(update_text).upper()
        # Menu option 1 - Change Title
        if menu_input == '1':
            # Gets new title info from title() function
            # Sends the new title info to the bookshop.py file update_title function to alter the field.
            title_update = title()
            bookshop.update_title(title_update, id_of_book)
        elif menu_input == '2':
            # Gets new author info from author() function
            # Sends the new author info to the bookshop.py file update_author function to alter the field.
            author_update = author()
            bookshop.update_author(author_update, id_of_book)
        elif menu_input == '3':
            # Gets new quantity info from quantity() function
            # Sends the new quantity info to the bookshop.py file update_quantity function to alter the field.
            quantity_update = quantity()
            bookshop.update_quantity(quantity_update, id_of_book)
        elif menu_input == 'S'or menu_input =='SAVE':
            # Commits any changes to the database through the bookshop.py commit_changes() function and saves.
            # It then breaks the loop and returns back to the main menu
            bookshop.commit_changes()
            print("\033[1;4mUpdates have been saved\033[0m, thanks. Returning to main menu.")
            break
        elif menu_input == 'X' or menu_input == 'EXIT':
        # Rolls back any changes using the bookshop.py rollback_changes() function does not save
        # Any changes made will be converted back to before the update began, and therefore will exit without saving
            # It then breaks the loop and returns back to the main menu
            bookshop.rollback_changes()
            print("\033[1;4mNo updates have been saved\033[0m, please try again to make changes! Returning to main menu.")
            break
        else:
        # if the user enters a key not in the menu, it will run the invalid_input() function and loop back to options again
            invalid_input()

# Function to delete a book. It searches by the unique id.
# Made the user identify the book by its primary key... This way each book is unique and there is no ambiguity
# The user can search or view all books to locate the id from the main menu.
def delete_book():
    id_of_book = input("What is the id of the book you would like to delete: ")
    # Searches for the book in the database using the bookshop.py search_id() function
    book = bookshop.search_id(id_of_book)
    # if no info is returned from the search, it will respond with such and go back to the main menu
    if book == []:
        print("No book found with that id, returning to main menu!")
    else:
        # Shows the book info if found, and double checks with the user that they want to delete it.
        print("\n\033[1;4mAre you sure you want to delete this book?\033[0m")
        print(tabulate(book, headers=["Book ID","Title", "Author", "Quantity"], tablefmt="pretty"))
        check = input("Yes(Y) / No (N): ").upper()
        # If 'y / yes' delete book through bookshop.py delete_row() function
        if check == 'Y' or check == 'YES':
            bookshop.delete_row(id_of_book)
            print("This book has been deleted from database!")
        # Any other key, will take you back to the main menu
        else:
            print("Book has not been deleted, returning to main menu.")

# function to search for book, this will find books by full title or parts of the title
def search_book():
    title = input("Enter book title (or part of the title to search): ")
    # sends user input to the bookshop.py search_books.py function
    book = bookshop.search_books(title)
    # if no data returned, then no book found and returns to main menu
    if book == []:
        print("No book found with the search criteria, returning to main menu!")
    else:
    # if info returned from database then display book / books using the tabulate pretty format 
        print("\n\033[1;4mTable returning books based on search query\033[0m")
        print(tabulate(book, headers=["Book ID","Title", "Author", "Quantity"], tablefmt="pretty"))

# Function that gets all the data from the ebookstore database and shows it to the user using the tabulate pretty format
def view_all_books():
    # gets all the information about the books using bookshop.py view_all_books() function
    books = bookshop.view_all_books()
    print("\n\033[1;4mTable to show all books in database\033[0m")
    print(tabulate(books, headers=["Book ID","Title", "Author", "Quantity"], tablefmt="pretty"))

# Function that says that an invalid option has been selected and to try again.
def invalid_input():
    print("Invalid input, please try again!")

# function used when closing the program to commit all changes to the database, save, and close the connection with the db 
def close_database():
    bookshop.commit_changes()
    bookshop.close_connection()
    print("The database has been saved and closed. Thank you for using the program.")

# Title function with while loop to get all the correct title information for a book.
# If no information or more than 80 characters are entered it will ask the user to try again
def title():
    while True:
        title = input("What would you like the title to be: ")
        if title == "":
            print("No information added, please try again!")
            continue
        if len(title) >= 80:
            print("Too much information added, please summarise to less than 80 characters and try again!")
            continue
        else:
            break
    return title

# Author function with a While loop to get all the correct author information for a book.
# If no information or more than 50 characters are entered it will ask the user to try again
def author():
    while True:
        author = input("Who is the author of the book: ")
        if author == "":
            print("No information added, please try again: ")
            continue
        if len(author) >= 50:
            print("Too much information added, please summarise to less than 50 characters and try again!")
            continue
        else:
            break
    return author

# Quantity function with a While loop to get all the correct quantity information for a book.
# If the input is not a positive integer below 100000 then it will ask the user to try again
def quantity():
    while True:
        qty = input("How many books are available: ")
        try:
            qty = int(qty)
        except:
            print("this is not an integer, please try again!")
            continue
        if qty < 0 or qty > 100000:
            print("Please enter a number between 0 and 100000, please try again!")
            continue
        else:
            break
    return qty


### GLOBAL VARIABLES ###

# global variable for the main menu text
menu_text = f'''------------------------------
-- Bookshop Database App --
1. Enter book
2. Update book
3. Delete book
4. Search books
5. View all books
0. Exit
Please select a number as an option: '''

# global variable for the update book menu text
update_text = f'''
-- Update options --

1 = Update Title
2 = Update Author
3 = Update Quantity

S = Save and Exit
X = Don't Save and Exit

Please select an option: '''

### MAIN PROGRAM ###

# run the functions in this order
# creates database and table (if not existing)
bookshop.create_tables()
# adds initial data or changes the original books to their default values. 
# This is so that the task is met and has the correct structure, and values according to the PDF.
# However, any new books added by users in the database will remain valid and use the previously saved inputted data. 
bookshop.add_initial_data()
# run menu function and the main program until '0' is chosen in the main menu
menu()
# When exiting the application - run close_database() function to correctly save the data and close the connection.
close_database()
