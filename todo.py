user_data=[]
# Welcome message 
print('Welcome to our Todo-App')

print('1.Add To-do \n' '2.View all todos')
user_action = input(('Enter a number from the menu list: '))
if user_action == "1":
    user_data.append(input('Enter your data: '))  
while True:
    # taking a data from a user
    # (passing the data to itself so that we could get hold of the data)
    user_data=user_data
    # Created a variable to help display the todos/data
    user_results = user_data
    # Displaying the data to the user
    print(user_results)
    print('Do you want to end?')
    # Ask if to end the program if the user wish to
    user_response=input(('Enter either True or False:' ))
    # condition to check if user typed true to stop the program 
    if user_response.capitalize() == "True":
        break
     # condition to check if user typed false for the program to run
    elif user_response.capitalize() == "False":
        user_data.append(input('Enter your data: '))

        

        
    
    
