import random

alphabet = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
];

numbers = ['0','1','2','3','4','5','6','7','8','9'];

specialChars = [
  '!','@','#','$','%','^','&','*','(',')','-','_','=','+',
  '[',']','{','}','\\','|',';',':','\'','"','<','>',',',
  '.','/','?','`','~'
];

desiredLetters=int(input("How many Letters would you like: "));

desiredNumbers=int(input("How many Numbers would you like: "));

desiredSpecial=int(input("How many Specials would you like: "));




newList=""

for x in range(desiredLetters):
    randomLet= alphabet[random.randint(0,len(alphabet)-1)]
    newList= newList + str(randomLet)

for x in range(desiredNumbers):
    randomLet= numbers[random.randint(0,len(numbers)-1)]
    newList= newList + str(randomLet)

for x in range(desiredSpecial):
    randomLet= specialChars[random.randint(0,len(specialChars)-1)]
    newList= newList + str(randomLet)

random.shuffle(list(newList))
print(newList)