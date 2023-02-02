user_data=[]
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
        user_data.append(input('Enter your data: '))

        

        
    
    
