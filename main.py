import random

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
print(HangWord)

for letter in HangWord: # for each letter in the Hangman Word 
    foundSimilar =False
    for similar in LetterBank: # Check if there is a letter in the bank thats similar
        if letter ==similar:
            foundSimilar =True #if found it doesnt add
            print("Found Similar")
    if foundSimilar==False:
        LetterBank = LetterBank+letter

print(LetterBank)
print(len(LetterBank))
while len(LetterBank)>0:
    print("Try Guessing a Letter")
    guess= input()
    if guess in LetterBank:
        print("Correct!")
        NewLetterBank= LetterBank.replace(guess,"")
        print(len(NewLetterBank))
        LetterBank= NewLetterBank
    print(LetterBank)
print("GAME OVER")