# # built in functions and user-defined functions
# # they are reuseable 

# # Why?
# # To break down your program into components and stop repeat codes

# # When?
# # when your codes turns to be plenty and unorganized we use function to break it down
# # pass is a keyword means nothing 
# #  How (Syntax)
# # def functionname (Parameters):
# '''
#  docstring
# '''
# # instructions
# # def addition(*num):
# #     """
# #     This function helps user to add two numbers and display the results
# #     """
# #     return num
# #     for nums in num:
# #         print(num)
    
# # results =addition(1,2)
# # print(results)

# # Assignment
# # Create a function that takes a list of numbers as argument and return the sum of those numbers
# def add(*nums):
#     i=0
#     s=0
#     while (i<len(nums)):
#         s=s+nums[i]
#         i+=1
#     print (s)
# add(1,5,2,1,12,31,41)

# # # Create a function that takes a string as an argument and returns a number of vowels in the string
# def count_vowels(string):
#     total_vowels = 0
#     for char in count_vowels:
#         if char in ['a','e','i','o','u']:
#             total_vowels=+1
#     print(total_vowels)


# # Create a function that takes in two strings as  an argument and returns a strings 
# # that contains a character that are common to both string.

# def common_char(inp_1,inp_2):
#     inp_1=set(inp_1)
#     inp_2 =set(inp_2)
#     return  inp_1.intersection(inp_2)

# results=common_char('Charles','Appiah')
# print(result


# # student_name and greeting
# function ==> 4 no's ==> returns the sum to the user

from main import age
print(name)