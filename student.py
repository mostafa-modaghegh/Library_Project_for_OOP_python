import book

def student(username=None):
    
    while True:
         
        print("""
    Welcome to student panel
      1. My books
      2. Available books        
      3. Search
      4. Book reservation   
      5. Return the book
      6. Log out
    """)
        
        try: 
            input_var = int(input("Enter choise between 1 to 6: "))
            if(input_var==1):
              book.my_books(username)
            elif(input_var==2):
              book.list_not_reserved_book()
            elif(input_var==3):
              book.search()
            elif(input_var==4):
              book.reserve_book(username)
            elif(input_var==5):
              book.return_book(username)
            elif(input_var==6):
              break         
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
           print("Invalid input. Please enter a number between 1 and 6.")
      