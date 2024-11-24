import book

def admin():

    while True:
    
       print("""
    Welcome to admin panel
    1. Add Book
    2. Edit Book
    3. Remove Book
    4. List of Books
    5. Inventory of Books         
    6. Search
    7. log out      
    """)
       try: 
            input_var = int(input("Enter choice between 1 to 7: "))
            if(input_var==1):
                book.add_book()
            elif(input_var==2):
                book.edit_book()
            elif(input_var==3):
                book.remove_book()
            elif(input_var==4):
                book.list_book()
            elif(input_var==5):
                book.inventory_book()
            elif(input_var==6):
                book.search()
            elif(input_var==7):
                break
            else:
                print("Please enter a number between 1 and 7")
       except ValueError:
           print("Invalid input. Please enter a number between 1 and 7.")

    


