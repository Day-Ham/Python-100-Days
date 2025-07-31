import sys
water=10000
milk=10000
coffee=100
money=0
price=0
def report():

    print("Water: " +str(water)+"ml")
    print("Milk: " +str(milk)+"ml")
    print("Water: " +str(coffee)+"g")
    print("Coffe: $" +str(money))

def manageresource(price,drink):
     match drink:
        case 'espresso':
            if water>100 and coffee>20:
                water-=100
                coffee-=20
            else:
                print("Option isnt Avaialable Refunding: $"+str(price))
        case 'latte':
            if water>400 and coffee>10 and milk>100:
                water-=400
                milk-=100
                coffee-=10
            else:
                print("Option isnt Avaialable Refunding: $"+str(price))

        case 'cappuccino':
            if water>300 and coffee>10 and milk>200:
                water-=300
                milk-=200
                coffee-=10
            else:
                print("Option isnt Avaialable Refunding: $"+str(price))
        case _:
            print("Option isnt Avaialable")
def askpayment( price,drink):
    print("Your Drink is "+ str(drink) +" that will be $"+str(price) )
    print("How much pennies do you have: ")
    pennies= int(input())
    print("How much nickles do you have: ")
    nickles= int(input())
    print("How much dimes do you have: ")
    dimes= int(input())
    print("How much quarters do you have: ")
    quarters= int(input())
    print("How much dollar do you have: ")
    dollar= int(input())
    total= (0.01 *pennies) + (0.05 *nickles) +(0.1 *dimes) +(0.25 *quarters)+dollar
    if total>price:
       print("Youre Change is: $" +str(total - price))

    else:
        print("Insufficient Funds")

def main():
    print("Select Which drink you would like to have espresso/latte/cappuccino:")
    choice=input()
    match choice:
        case 'report':
            report()
        case 'espresso':
            askpayment(1.50,'espresso')
            
        case 'latte':
            askpayment(2.75,'latte')
            
        case 'cappuccino':
            askpayment(2.60,'cappuccino')
            
        case 'quit':
            sys.exit()
        case _:
            print("Option isnt Avaialable")

main()