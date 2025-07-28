import random
import os

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
PlayerTotal=0
PlayerTotalLower=0
DealerTotal=0
DealerTotalLower=0
PlayerHand=[]
DealerHand=[]
command='hit'
def ConvertToTotal(hand):
    total=0
    for card in hand:
        if card== 'J' or card== 'Q' or card== 'K':
            total+=10
        elif card== 'A':
            total
        else:
            total += int(card)
    
    return total
        
while command =='hit':
    os.system('cls')
    PlayerHand.append(ranks[random.randint(0,len(ranks)-1)])
    PlayerTotal= ConvertToTotal(PlayerHand)
    print(PlayerHand)
    print("Total is: " + str(PlayerTotal))
    if PlayerTotal >21:
        print("Player Bust")
        break
    elif PlayerTotal == 21:
        print("Black Jack Player Wins")
        break
    print("Would you like to Hit or Stand")
    command=input()

if PlayerTotal<21:
    while DealerTotal<21:
        os.system('cls')
        DealerHand.append(ranks[random.randint(0,len(ranks)-1)])
        print("Dealer Hand")
        print(DealerHand)
        print("Player Hand")
        print(PlayerHand)
        DealerTotal= ConvertToTotal(DealerHand)
        print("Dealer Total is: " + str(DealerTotal))
        print("Player Total is: " + str(PlayerTotal))
        if DealerTotal==21:
            print("Black Jack Dealer Wins")
            break

if DealerTotal>21:
    print("Dealer Bust, Player Wins")
