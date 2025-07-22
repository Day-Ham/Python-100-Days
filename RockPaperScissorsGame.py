import random

print("Pick a Number")
print("1. Rock")
print("2. Paper")
print("3. Scissor")


while True:
    player= input()
    try:
        player=int(player)
        match player:
            case 1:
                print("You picked Rock")
                break;

            case 2:
                print("You picked Paper")
                break;

            case 3:
                print("You picked Scissors")
                break;
            case _:
                print("You picked none of the choices try again")
    except ValueError:
        print("Please use a Number")
        
player=int(player)
bot= random.randint(1,3)
match bot:
            case 1:
                print("Bot picked Rock")
            case 2:
                print("Bot picked Paper")
            case 3:
                print("Bot picked Scissors")




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
else:
    print("You pick outside the choices you are disqualified")