
# List
# List are used to store different types of data values
# They are organized and mutable

# # creating a list in python
# name=['joel',1,2,False,21]
# name[0]=("Charles")
# print(name)


# # Write a list of 10 numbers and use a  for loop to print each number
# # Write a list of 10 numbers a use the bulit in sum function to find the sum of all the numbers
# # Write a list of 10 numbers a use the bulit in min and max function to find the smallest and largest numbers in the list
# # Create a list of 10 random numbers and use a for loop to print the square of each number
# # Write a list of


# # Write a list of 10 numbers and use a  for loop to print each number
# person= ['Joel','Kofi Badu','John','Charles']
# for names in range(len(person)):
#     print(person[names])

# # #  Write a list of 10 numbers a use the bulit in sum function to find the sum of all the numbers
# num=[1,2,3,4,5,6,7,8,9,10]
# print(sum(num))

# # Write a list of 10 numbers a use the bulit in min and max function to find the smallest and largest numbers in the list
# num=[2,22,33,44,55,64,27,48,129,10]
# print(min(num))
# print(max(num))

# # Create a list of 10 random numbers and use a for loop to print the square of each number
import random
number =[]

for i in range(0,10):
   number.append(random.randint(1,10)**2)
   print(number[i])


# List helper methods
# append    count
# index     copy
# clear     insert
# copy      pop

numbers = [2, 6, 9]
numbers.count(0)
print(numbers)
# List Slicing
# It helps you get portion of a list
numbers=[3,4,5,7,1,8]
print(numbers[-1:0])
# Tuple
# Tuple allows you to store items  with different data types
# Tuple are organized
# Tuple are immutable

# numbers =(2,4,6,9)

# Sets
# Sets are used to store values and different data types

