'''
You are managing a small library and want to keep track of the books
available. Every time a user wants to borrow a book, you need to check
if the book exists and if there are any copies left. Use a dictionary
to store this information.
'''

'''
Create a Book class and initialise a constructor that takes in 3
arguments for the book title, author, and number of copies. Inside
the constructor, initialise the necessary instance variables. Also
add a copy_in_library method for the Book class that checks if
there is at least one copy of the book available.
'''

class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def copy_in_library(self):
        return self.copies > 0 # return True if there is at least one copy, False otherwise

'''
Initialise an empty variable called library of type dictionary
to store and access book objects:
   - the key is the title of the book.
   - the value is an instance of the Book class.
'''
library = {}

'''
Create the following functions:


 1. populate_library() - a function that adds 3 books to the library
    dictionary. Just as in the task, at program start-up, this
    function should be used to populate your library with three sample
    book objects for further use in your program. This function does
    not need to be included as a menu option for the user.


 2. list_books() - a function that loops through the library
    dictionary and prints each book's title, author, and how many
    copies are available.


 3. list_available_books() - a function that lists only books that
    have at least one copy available.


 4. borrow_a_book() - the user enters the title of the book they want
    to borrow, and the function checks if the book is in the library
    and if there are copies available.
'''

def populate_library():
    library["Atomic Habits"] = Book("Atomic Habits", "James Clear", 3)
    library["Brave New World"] = Book("Brave New World", "Aldous Huxley", 0)
    library["The Twilight Saga"] = Book("The Twilight Saga", "Author name", 10)

def list_books():
    for title, book in library.items():
        print(f"Title: {title} Author: {book.author} Number of copies: {book.copies}")

def list_available_books():
    for title, book in library.items():
        if book.copy_in_library():
            print(f"Title: {title} Author: {book.author} Number of copies: {book.copies}")

def borrow_a_book(title):
    if title in library and library[title].copy_in_library():
        library[title].copies -= 1
        print(f"You have borrowed {title}.")

    else:
        print("That book does not exist.")

'''
Create a simple main menu that gives the user options to list books, view available books,
borrow a book, or quit the application (these will be the menu options).
'''

# We need to get some books in our library
populate_library()

while True:
    print("1. List all books")
    print("2. List available books")
    print("3. Borrow a book")
    print("4. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        list_books()

    elif choice == '2':
        list_available_books()

    elif choice == '3':
        user_title = input("Enter the title of the book you would like to borrow: ")
        borrow_a_book(user_title)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")