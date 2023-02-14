
container=[]

container.append(input(('Enter your number: ')))
container.append(input(('Enter your number: ')))
print(container)

# Function to add list to Todo's
def add_list():
    container.append(input(('Enter your number: ')))
    data=container
    print('Added a Todo!')

# Function to view list
def view_list():
    for i in range (len(container)):
     print(container[i])

def delete_list():
        user_input=container
        user_input.remove((input('Enter the number you want to delete: ')))
        print(f'todo has been deleted successfully !')
        data=container
        print(f'{data} is the remaining list')
        user_deleted=input('Do you want to view deleted todo? Yes or No ')
        if user_deleted == 'Yes':
            print(f'{user_input}')


# # Function to update list in a today list
def update_todo():
    container.insert((len(container)),input('Enter your new todo to update the list: '))
    update_todo=container
    print(update_todo)

update_todo()