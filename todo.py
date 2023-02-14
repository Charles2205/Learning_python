<<<<<<< HEAD
user_data=[]
import todo_functions

print('Welcome to our Todo-App')
print('1.Add To-do \n' '2.View all todos')
user_action = input(('Enter a number from the menu list: '))
if user_action == "1":
    user_data.append(input('Enter your data: '))  
while True:
    user_data=user_data
    user_results = user_data
    print(user_results)
    print('Do you want to end?')
    user_response=input(('Enter either True or False:' )) 
    if user_response.capitalize() == "True":
        break
    elif user_response.capitalize() == "False":
        user_data.append(input('Enter your todo heres: '))

        

        
    
    
=======
from colors import GREEN, RED, YELLOW, WHITE 
def welcome_screen():
    print('** Welcome to our Todo App ***')
    user_input(int(input('Enter a a valid value from the list below \n1.Manage Todo\n2.About Todo\n3.Exit Apllication')))



def determine_user_input(user_input):
    
    if user_input == 1:
       pass
    elif user_option == 2:
        pass
    elif user_option == 3:
        pass
    else:
        pass
>>>>>>> 84ed8150f53bd250a172b8e335e1265a2a6ce8e3
