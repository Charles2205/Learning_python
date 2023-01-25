# # assignment
# user_input = input("Enter an integer: ")
# user_int = int(user_input)
# print(user_int)

# Question 1
# alphabet=input("Enter alphabet: ")
# if alphabet in ['a','e','i','o','u']:
#     print('Vowel')
# else:print("consonant")

# # Question  2
# user_number=int((input('Enter your number: ')))
# if user_number % 2 == 0:
#     print('is a prime number')
# else:print("The number you've entered is not a prime number")

# # Question 3
# year=int(input('Enter year: '))
# if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
#     print('Leap year')
# else:print('Not a leap year')

# text=str((input('Enter a word: ')))
# Palindrome_check=text[::-1]
# if text == Palindrome_check:
#     print('Palindrome')
# else:print('Not a palindrome')

# # Question 5
# fahrenheit=float((input('Enter the temperature: ')))
# celsius =(fahrenheit-32)*5/9
# if fahrenheit<32:
#     print('freezing')
# elif fahrenheit>212:
#     print('boiling')
# else:
#     print('temperature in celsius')

#     #Question 6
# password =str(input('Enter your password'))
# if len('password') >8:
#     password.search=str("[a-z]")
#     password.serach=str("[A-Z]")
#     password.search=int("[0-9]")
#     print('password accepted')

# else:
#     print('password not accepted') 







# Today's Assignmnent

# user_number= int(input("enter your number:"))
# n=1
# while n>=1:
#     n=n*1
#     n=n-1
#     print(n)

user_number = int(input("please enter whole number value : "))
total = 0
number = 1
while number <= user_number:
     if (number % 2 == 0):
        print(number)
        total = total + number
     number += 1

print(f"the sum of even numbers = {total}")




# n=int(input())
# sum=0
# i=1
# while i<=n:
#       if(i%2==0):
#              sum+=i

factorial=1
n=1
while True:
    num=int(input("Enter number: "))
    if num<=0:
        print("Thank you!")
        break
    while n<num:
        n+=1
        factorial*=n
    print(factorial)