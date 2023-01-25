# for loops # while loops
# Using while loop in python 
# continue and break loops


# counter = 1
# while counter <= 100:
#     print(counter)
#     counter += 1
    # PROMPT A USER REPEATELY UNTILL  THEY ENTER A NUMBER GREATER THAN 100
    # how to get user number
    
# while True:
#         user_input=int((input('Enter a number: ')))
#         if user_input >100:
#             break

# # For Loops in python
# for i in range(1,11,):
#     print(i) 

   # Write a program to find the sum of 1 to 100  
# sum=0
# for i in range(1,101):
#    sum=sum + i

# print(sum)

# Write a program to find all the even numbers between 1 and 100 
# for i in range(2,102,2):
#     print(i)
 
#write a program to accept a number from a user determine all the even numbers between 1 and the number
user_input=int((input('Enter a number: ')))
for i in range(2,user_input):
    if i%2==0:
        print(i)
