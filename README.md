# E-bookstore Database Simulation - Final Capstone

An e-bookstore simulation for demonstrating competence using Python and SQL.

## Description

A program for a bookstore that allows users to view/add/remove/edit/data about the books they have in the inventory. This has a search facility and shows the availability of books based on the database.

## Table of contents
1. Installation
2. Loading the program
3. How to use the bookstore database
    * Enter book
    * Update book
    * Delete book
    * Search books
    * View all books
    * Exit
4. Help
5. Credits
6. Version History

### 1. Installation

Download the three program files from the [finalCapstone](https://github.com/garethreece/finalCapstone) repository into a directory of your choosing. They need to be in the same directory.
* bookshop.py
* bookstore_app.py
* ebookstore.db

Most operating systems or python packages have SQLite and tabulate installed as standard. However, if you are having problems running the files then you might need to install them. Links are included with instructions.
* [SQLite](https://www.sqlite.org/index.html)
* [Tabulate](https://pypi.org/project/tabulate/)

### 2. Loading the Program

Open the file **bookstore_app.py** into an IDE and run the program. The program menu will come up in the terminal window. The image below shows the code being run and the opening terminal.

![Screenshot of program being run in visual studio](https://github.com/garethreece/finalCapstone/blob/main/Images/running%20program.jpg)

If this doesn't work see the installation guide

### 3. How to use the bookstore database

You will be greeted with a menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
5. View all books
0. Exit
Please select a number as an option:

Select a numbered option.

1) Enter Book  - You are given three prompts
* Add Title
* Add Author
* Add Quantity

Enter the relevant inputs into these prompts and it will add the book and quantity. An ID (and primary key) is automatically assigned as the next digit up from the last book.

![Screenshot of adding a book](https://github.com/garethreece/finalCapstone/blob/main/Images/add%20book.jpg)

2) Update book

Select option number 2 and it will ask you for the id of the book to edit. If you don't know the id you can use the search or view all selections in the main menu to find it.
Once you have added a recognisable id it will confirm if this is the book you want to edit (Y/N). If Yes, then you will be presented with three edit options, update title, author, quantity... or you can save and exit or just exit without saving

![Screenshot of updating a book](https://github.com/garethreece/finalCapstone/blob/main/Images/update%20book.jpg)

You can alter the information for each edit option as much as you want. However, it will only save the changes to the database if you chose 'Save and Exit' Otherwise, Don't Save and Exit will revert to before the update.

3. Delete Book

This is done by searching for the ID of the book (use the search or view all from the main menu if you don't know the ID). If a recognisable id is entered into the prompt, then it will show the user the book and clarify if this is the book that is to be deleted (Y/N). If Yes, will remove from the database and return to the main menu, if no, nothing will be changed in the database.

4. Search books

The 'search books' for this database matches any information in the title. You can enter the whole title or parts of the title to search. It will return anything that matches the search criteria in a nice table format. 

![Screenshot of searching a book](https://github.com/garethreece/finalCapstone/blob/main/Images/search%20book.jpg)

5. View all books
This shows all the books in the database in a table format including id and quantity. If there are a lot of books in the database this could be a big list!

![Screenshot of searching a book](https://github.com/garethreece/finalCapstone/blob/main/Images/view%20all%20book.jpg)

0. Exit

This will close the program and commit any changes to the database, saving whatever has been modified for the next time the user opens the program.

### 4. Help

Feel free to contribute, edit, and use the program. If there are any concerns, contact garethreece@hotmail.com and I will attempt to resolve the issue as soon as possible.


### 5. Credit
Programmer - Gareth Reece - garethreece@hotmail.com [@github/garethreece](https://github.com/garethreece)<br>
Client - HyperionDev - [www.hyperiondev.com](www.hyperiondev.com)

### 6. Version History

* 0.2
    * Various bug fixes and optimisations
    * See [commit change](https://github.com/garethreece/finalCapstone/commits/main) or See [release history](https://github.com/garethreece/finalCapstone/releases)
* 0.1
    * Initial Release 16-02-2023
