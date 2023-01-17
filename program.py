# first_name=input('Enter your first name: ')
# last_name=input('Enter your last name: ')
# print(first_name.upper())
# print(last_name.lower())

# email=input('Enter your email: ')
# email_split=email.split('@')
# print(name_split[0])


# assignment
# user_input = input("Enter an integer: ")
# user_int = int(user_input)
# print(user_int)

# strip method
# it is used to remove spaces at the begining and ending of a results the user types...
# name=input('User Name: ')
# print(name.strip())

# Count 

# length 
# first_name= input('Enter your first name: ')
# last_name= input('Enter your last name: ')
# print (len(first_name.strip()))
# print (len(last_name.strip()))

# f_name=input('Enter your first name: ')
# l_name=input('Enter your last name: ')
# age = int(input('Enter your age: '))
# full_name=f_name+' '+l_name
# print(f'Your full name  is {full_name} and your age is {age}')

# type casting 
# str
# int
# float
# bool

# Write a program to accept three numbers from a user and display them the sum,product and average of the three numbers
# question 1
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print (f'sum= {sum}')
print (f'product = {product}')
print (f'average= {average}')

# question 2
str_x="Emma is a good developer.Emma is a writer"
print(f"The word Emma appeared {str_x.count('Emma')} twice")

# question 3
num1=4
num2=4
results =num1*num2/2
print(f'the final results is {results}')

# Question 4
first_name=input("enter your first name:")
last_name=input("enter your last name: ")
print(first_name.upper()+" "+last_name.lower())