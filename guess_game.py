# adding the random module file into our project
import random

# generate a random from 1-100
gen_number=random.randint(1,10)
# count user guesses
user_guess_count=0

while True:
# Accepting user guessed number
    user_input=int((input('Enter your number: ')))
# determing if user's guess is correct
    if user_input==gen_number:
        print('Congratulations !!! You guessed right')
        break
    elif user_input>gen_number:
        print('Too high.Try again')
    elif user_input<gen_number:
        print('Too low.Try again')
    if user_guess_count == 4:
        print ('Reset ')
        break
    user_guess_count+= 1 
print(f'the number of wrong guesses is {user_guess_count}')