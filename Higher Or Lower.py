import random 

NumberToGuess = random.randint(0,100)
LivesLeft=5
Guess=0
print("Welcome would to Higher or Lower would you like to play easy or hard")
Choice=input()
if Choice=='easy':
     LivesLeft=10
elif Choice=='hard':
    LivesLeft=5
else:
     LivesLeft=10
     
while LivesLeft>0 and Guess!=NumberToGuess:
    print("You have " + str(LivesLeft)+" Lives Left")
    print("Guess a Number")
    Guess=int(input())

    if Guess> NumberToGuess:
        print("You are Higher than the number")
    elif Guess< NumberToGuess:
        
        print("You are Lower than the number")
    if Guess!=NumberToGuess:
        
        LivesLeft-=1
if LivesLeft ==0:

    print("Game Over No more Lives")
    print("The Number was " + str(NumberToGuess))