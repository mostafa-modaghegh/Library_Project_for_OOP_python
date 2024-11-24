from enum import Enum
from collections import Counter

class Book:
    def __init__(self, book_id, book_name, book_type, reserved=False, studentName=None):
        self.book_id = book_id
        self.book_name = book_name
        self.book_type = book_type
        self.reserved = reserved
        self.studentName = studentName

class Book_Type(Enum):
    Software = 1
    Network_and_security = 2
    Artificial_Intelligence = 3
    Hardware = 4

Books_List = []

def add_book():
    book_name = input("Enter name of book: ")
    print("""
        1. Software
        2. Network and Security
        3. Artificial Intelligence
        4. Hardware
    """)
    while True:
        try:
            input_var = int(input("Enter choice between 1 to 4: "))
            if 1 <= input_var <= 4:
                book_type = Book_Type(input_var).name
                break
            else:
                print("Please enter a valid choice between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    book_id = 1 if not Books_List else max(book.book_id for book in Books_List) + 1
    new_book = Book(book_id, book_name, book_type)
    Books_List.append(new_book)
    print(f"{book_name} added to the list of books successfully.")

def edit_book():
    try:
        input_var = int(input("Enter the ID of the book you want to edit: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return


    indexes_list = [book.book_id for book in Books_List]

    if input_var in indexes_list:
        edited_name = input("Enter the new name of the book: ")
        while True:
            try:
                input_type = int(input("Enter choice between 1 to 4 for the new book type: "))
                if 1 <= input_type <= 4:
                    edited_type = Book_Type(input_type).name
                    break
                else:
                    print("Please enter a valid choice between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        for book in Books_List:
            if book.book_id == input_var:
                book.book_name = edited_name
                book.book_type = edited_type
                print(f"Book ID {book.book_id} updated successfully.")
                return
    else:
        print("No book found with the given ID.")


def remove_book():
    try :
        input_var = int(input("Enter the ID of the book you want to remove: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return   
    
    indexes_list = [book.book_id for book in Books_List]

    if input_var in indexes_list:
        Books_List.pop(input_var-1)
        print(f"Book ID {input_var-1} removed successfully.")
    else:
        print("No book found with the given ID.")


def list_book():
    for book in Books_List:
        print(f"""
              Id: {book.book_id} name: {book.book_name} type: {book.book_type}
            resreved: {"True" if book.reserved else "False"} student Name: {book.studentName if book.studentName!=None else "_"}
            **********
""")
        

def inventory_book():
    books = []
    for b in Books_List:
        books.append(b.book_name.lower())

    counted = Counter(books)
    result = list(counted.items())
    print(result)


def list_not_reserved_book():
    not_reserved_books = []
    for b in Books_List:
        if(b.reserved==False):
            not_reserved_books.append(b.book_name.lower())

    counted = Counter(not_reserved_books)
    result = list(counted.items())
    print(result)


def search():
    input_search = input("Enter the phrase you want to search: ")
    search_list = []

    for book in Books_List: 
        if input_search.lower() in book.book_name.lower(): 
            found_book = {"ID": book.book_id, "Name": book.book_name, "Reserved": "Yes" if book.reserved else "No"}
            search_list.append(found_book)


    if search_list:
        for book in search_list:
            print(book)
    else:
        print("No books found matching your search.")

def my_books(username):
    my_books = []
    for book in Books_List:
        if book.studentName == username:
            my_books.append(book)
    for book in my_books:
        print(f"book: {book.book_name} type: {book.book_type}")        

def reserve_book(username):
    try:
        input_var = int(input("Enter the ID of the book you want to reserve: "))
    except ValueError:
        print("Invalid input. Enter a numeric value")
        return

    indexes_list = [book.book_id for book in Books_List]

    if (input_var in indexes_list):

        for book in Books_List:
            if (book.book_id==input_var):
                if (book.reserved==False):
                    book.reserved = True
                    book.studentName = username
                    print(f"{book.book_name} reserved successfully.")
                    break
                else:
                    print("This book is already reserved.") 
                    break   

    else:
        print("No book found by this index")

    
def return_book(username):
    try:
        input_var = int(input("Enter the ID of the book you want to return: "))
    except ValueError:
        print("Invalid input. Enter a numeric value")
        return


    indexes_list = [book.book_id for book in Books_List]

    if (input_var in indexes_list):

        for book in Books_List:
            if (book.book_id==input_var):
                if (book.studentName==username):
                    book.reserved = False
                    book.studentName = None
                    print(f"{book.book_name} returned successfully.")
                    break
                else:
                    print("This book has not been reserved by you.") 
                    break   

    else:
        print("No book was found by this index")
      
