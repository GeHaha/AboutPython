# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:36:09 2018

@author: Administrator
"""
import random
secretNumber = random.randint(1,20)
print('im thinking of a number between 1 and 20')

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print('your guess is too low')
        
    elif guess > secretNumber:
        print('Your guess is too high.')
        
    else:
        break
    
if guess == secretNumber:
    print("good job! you guessed my number in " + str(guessesTaken) +  'guesses!')
    
else:
    print('Nope. The number i was thinking of was ' + str(secretNumber))
    
    
        


