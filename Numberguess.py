print("Number Guessing Game")
import random
number = random.randint(1,9)
print("Guess any number between 1&9")
chance=0

while(chance<5):
    guess=int(input("Enter your guess"))
    if(number==guess):
        print("Congratulaion U Won!!")
        break
    elif(number<guess):
        print("Guess number less than ",guess)
    else:
        print("Guess Greater than ",guess)
    chance+=1

if(chance==5):
    print("You Lose the Game .The number is",number)    