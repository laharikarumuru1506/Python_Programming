import random
import math

#taking inputs by the user
upper=int(input("enter the upper bound: "))
lower=int(input("enter the lower bound: "))
#complier choose one number from the range given by the user
num=random.randint(lower,upper)
print("you've",round(math.log2(upper-lower+1)),"chances to play the game")
for i in range(round(math.log2(upper-lower+1))):
    guess=int(input("enter the guessed number: "))
    if guess==num:
        print("Congratulations!you guessed the right number at ",i,"chance")
        break
    elif guess<num:
        print("Try again!you guessed too small")
    else:
        print("Try again!you guessed too high")
else:
    print("Better luck next time!")
    print("And the guessing number is ",num)
