import os
import time
from question_model import Question
from data import trivia
Question_Bank=[]
Lives=3

for item in trivia:
    NewQuestion=Question(item["question"],item["answer"])
    Question_Bank.append(NewQuestion)
os.system('cls')
for question in Question_Bank:
    print("Lives Left: " +str(Lives))
    print(question.text)
    answer= str(question.answer).lower()
    guess =  str(input()).lower()
    if guess==answer:
        print("Correct!")
    else:
        print("Incorrect!")
        Lives -=1
    if Lives==0:
        break
    time.sleep(1)
    os.system('cls')

os.system('cls')
if Lives>0:
    print("You Win!")
else:
    print("You Lose!")