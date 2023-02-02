
container=[]
# def add_list():
    
#     container.append(input(('Enter your number: ')))
#     data=container
#     print('Added a Todo!')

# def view_list():
#     for i in range (len(container)):
#      print(container[i])

# container=view_list()
def delete_list():
        container.append(input(('Enter your number: ')))
        container.append(input(('Enter your number: ')))
        print(container)
        user_input=container
        user_input.remove((input('Enter the number you want to delete: ')))
        print(f'todo has been deleted successfully !')
        data=container
        print(f'{data} is the remaining list')
        
        user_deleted=input('Do you want to view deleted todo? Yes or No ')
        if user_deleted == 'yes':
            print(F'{user_input}')

# print( container)

delete_list()



# c_list=[1,2,3]
# print(c_list.remove(1))
# print(c_list)