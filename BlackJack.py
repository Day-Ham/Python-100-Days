import random
import os

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


PlayerMoney=2500.0
Bet=00.0
file_path="blackjacksave.txt"
GameLoop=True

def ConvertToTotal(hand):
    total=0
    for card in hand:
        if card== 'J' or card== 'Q' or card== 'K':
            total+=10
        elif card== 'A':
            total +=11
        else:
            total += int(card)
    
    return total
        
while GameLoop==True:
    PlayerTotal=0
    PlayerTotalLower=0
    DealerTotal=0
    DealerTotalLower=0
    PlayerHand=[]
    DealerHand=[]
    command='hit'
    print("Player Money: $" + str(PlayerMoney))
    print("How much would you like to bet")
    Bet=float(input())

    while command =='hit':
        os.system('cls')
        print("Player Money: $" + str(PlayerMoney))
        PlayerHand.append(ranks[random.randint(0,len(ranks)-1)])
        PlayerTotal= ConvertToTotal(PlayerHand)
        print(PlayerHand)
        print("Total is: " + str(PlayerTotal))
        if PlayerTotal >21:
            print("Player Bust")
            PlayerMoney -= Bet
            break
        elif PlayerTotal == 21:
            print("Black Jack Player Wins")
            PlayerMoney += Bet *1.5
            break
        print("Would you like to Hit or Stand")
        command=input()

    if PlayerTotal<21:
        while DealerTotal<21:
            os.system('cls')
            print("Player Money: $" + str(PlayerMoney))
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
                PlayerMoney -= Bet
                break

    if DealerTotal>21:
        print("Dealer Bust, Player Wins")
        PlayerMoney += Bet *1.5
    
    print("Would you like to continue? Y/N")
    choice =input()
    if choice=='n':
        GameLoop=False