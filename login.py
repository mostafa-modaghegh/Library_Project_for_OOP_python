import admin
import student

def admin_login():
   admin_name= "admin"
   admin_password= "adminadmin"
   i=1
   while i<=3:
       name= input("Enter your name: ")
       password= input("Enter your password: ")
       if(name == admin_name and password == admin_password):
           admin.admin()
           break
       else:
           print("Username or Password is not correct!")
           i += 1
   if(i==4):
      print("Sorry, Please try again later")
            

def student_login():
   user1 = [1,"username1","1234","Ali Ahmadi"]
   user2 = [2,"username2","5678","Reza Alizadeh"]
   i = 1
   while i<=3:
      name = input("Enter your name: ")
      password = input("Enter your password: ")
      if((name==user1[1] and password==user1[2])or(name==user2[1]and password==user2[2])):
        student.student(name)
        break
      else:
         print("Username or Password is not incorrect!")
         i += 1

   if(i==4):
      print("Sorry, Please try again later")
