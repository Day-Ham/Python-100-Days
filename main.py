import sys
water=100
milk=100
coffee=100
money=0
price=0
def report():

    print("Water: " +str(water)+"ml")
    print("Milk: " +str(milk)+"ml")
    print("Water: " +str(coffee)+"g")
    print("Coffe: $" +str(money))

def manageresource(penny,nickel,dime,quarter):
    print("")
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
       print(total - price)
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
            report()
        case 'latte':
            askpayment(2.75,'latte')
            report()
        case 'cappuccino':
            askpayment(2.60,'cappuccino')
            report()
        case 'quit':
            sys.exit()
        case _:
            print("Option isnt Avaialable")

main()