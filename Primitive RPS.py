import random

print("Pick a Number")
print("1. Rock")
print("2. Paper")
print("3. Scissor")

player= input()
match player:
    case 1:
        print("You picked Rock")

    case 2:
        print("You picked Paper")

    case 3:
        print("You picked Scissors")
player=int(player)

bot= random.randint(1,3)
if bot== 1 and player==3:
    print("Bot Wins")
elif bot== 1 and player==2:
    print("Player Wins")

elif bot== 2 and player==3:
    print("Player Wins")
elif bot== 2 and player==1:
    print("Bot Wins")

elif bot== 3 and player==1:
    print("Player Wins")
elif bot== 3 and player==2:
    print("Bot Wins")

elif bot== player:
    print("Draw")