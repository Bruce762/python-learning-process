
from question import Question#指引入特定東西，Question是一個class

text = [
    "what youra name\n(a)\n(b) \n(c)\n"
]
questions =[
    Question(text[0],"a")
]

def runtest(questions):
    score=0
    for question in questions:
        answer= input(question.des)
        if answer ==question.ans:
            print("good")
        else:
            print("bad")

runtest(questions)