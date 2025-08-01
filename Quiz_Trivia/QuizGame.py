from question_model import Question
from data import trivia
Question_Bank=[]
for item in trivia:
    NewQuestion=Question(item["question"],item["answer"])
    Question_Bank.append(NewQuestion)

print(Question_Bank[0].answer)