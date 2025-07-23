import random
import os
words = [
    "python",
    "hangman",
    "developer",
    "keyboard",
    "function",
    "variable",
    "algorithm",
    "condition",
    "syntax",
    "iteration",
    "object",
    "inheritance",
    "recursion",
    "boolean",
    "integer",
    "compiler",
    "exception",
    "parameter",
    "argument",
    "loop",
    "letter",
    "success",
    "banana",
    "committee",
    "balloon",
    "mississippi",
    "bottle",
    "gossip",
    "muffin",
    "kettle",
    "pepper",
    "noodle",
    "butter",
    "address",
    "bookkeeper"
]




HangWord= words[random.randint(0,len(words))]
LetterBank=""

for letter in HangWord: # for each letter in the Hangman Word 
    foundSimilar =False
    for similar in LetterBank: # Check if there is a letter in the bank thats similar
        if letter ==similar:
            foundSimilar =True #if found it doesnt add
    if foundSimilar==False:
        LetterBank = LetterBank+letter

Lives=5
RenderedWord =[]
for space in HangWord:
    RenderedWord.append("_")
while len(LetterBank)>0 and Lives>0:
    print("Lives Left: "+ str(Lives))
    GraphicWord= ''.join(RenderedWord)
    print(GraphicWord)
    print("Try Guessing a Letter")
    valid=False
    while valid==False:
        guess= input()
        if len(guess)>1:

            print("Must be ONE Letter")
        elif guess.isalpha()==False:

            print("Must be A Letter")
        else:
            valid=True

    os.system('cls')


    if guess in LetterBank:
        print("Correct!")
        NewLetterBank= LetterBank.replace(guess,"")
        LetterBank= NewLetterBank
        index=0
        for matchingLetter in HangWord:
            if matchingLetter == guess:

                RenderedWord[index]= matchingLetter
            index+=1









    else:
        print("Incorrect")
        Lives=Lives-1
        


os.system('cls')
print("GAME OVER")

if Lives==0:
    print("Word was: " +HangWord)
elif len(LetterBank)==0:
    print("You Guessed it!")