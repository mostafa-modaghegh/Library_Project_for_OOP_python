import sys
import login

def main():
    while True:
        print("Library management Program")
        print("1. Login as admin")
        print("2. Login as student")
        print("3. Exit")
        while True:
            try:
                input_var = int(input("Select choise between 1 to 3: "))
        
                if input_var==1:
                    login.admin_login()
                    break
                elif input_var==2:
                    login.student_login()
                    break
                elif input_var==3:
                    sys.exit()
                else:
                    print("Please Enter your login method correctly")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")

main()