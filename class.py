# class Person:
#     """This is a class to represent a person object"""
#     # defining the attributes of the person
#     first_name=''
#     last_name=''
#     age = 0
#     def move(self):
#         print('You can move')
#     def eat(self):
#         print('You can eat!!!')
# # Create object
# person1=Person()
# person1.first_name='Joel'
# person1.last_name='Badu'
# person1.age=56
# print(person1.first_name,person1.last_name)


# person2=Person()
# person2.first_name='Kofi'
# person2.last_name = 'Badu'
# person2.age=33
# print(person2.first_name,person2.last_name)



class User:
    """This is a class to represent a person object"""
    # defining the attributes of the person
    first_name=''
    last_name=''
    age = 0
    def __init__(self,fn,ln,age):
        self.first_name=fn
        self.last_name=ln
        self.age=age

    def hello(self):
        print(self.first_name)

user1 =User('Stephen','Charles',20)