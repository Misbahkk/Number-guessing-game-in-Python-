#Number guessing game in Python 3
import random
import math
print('Enter the range taht you guse the Number..')
lowe_bound = int(input('Enter the 1st number of range: '))
uper_bound = int(input('Enter the 2nd number of range: '))
guse_number = random.randint(lowe_bound,uper_bound)
count = 0
chance = math.log(uper_bound - lowe_bound +1,2)
print(f'You Have only {round(chance)} chance for guse the number')
while(count<chance):
    count+=1
    user_guse = int(input('Guse A Number: '))
    if user_guse >guse_number:
        print('Try Again! Your Guse too High...')
    elif user_guse <guse_number:
        print('Try again! your guse number too Short..')
    else: 
        print(f'Congrats! Your guse is correct, you try {count} times.')
        break
print(f'You try {chance} time! Better Than next time')
