print("Welcome To the Tip Calculator!")
print("What was the total bill?")
bill =00.0;
while True:
    bill= input()
    try:
        bill = float(bill)
        break;
    except:
        print("Please Use a number")
print("How Much would you like to tip? 10%, 12%, 15%?")

percent=0
while True:
    percent= input()
    try:
        percent = int(percent)
        break;
    except:
        print("Please Use a number")


print("How many people will split the bill")
participants=0
while True:
    participants= input()
    try:
        participants = int(participants)
        break;
    except:
        print("Please Use a number")
percent = float(percent)
percent= percent/100
percent= 1+percent
total = float(bill*percent)
split= total/participants
total= str(round(total, 2))
split= str(round(split, 2))

print("Total is $" + total)
print("That is $" + split +" among us" )