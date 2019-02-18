import random
class ChatBot:
    learning={}
    def __init__(self,standardanswer,questionanswer):
        self.standardanswer=standardanswer
        self.questionanswer=questionanswer
    def reply(self,text):
        if "?" in text:
            random_ans=random.randint(0,len(self.questionanswer)-1)
            print(self.questionanswer[random_ans])
        else:
            random_ans=random.randint(0,len(self.standardanswer)-1)
            print(self.standardanswer[random_ans])
    def learn(self):
        print("what is your name?")
        name=input()
        ChatBot.learning["name"]=name
        print("what is your lastname?")
        lastname=input()
        ChatBot.learning["lastname"]=lastname
        print("nice to meet you "+ChatBot.learning["name"]+" "+ChatBot.learning["lastname"])

Question_ans=["it's rainy","it's sunny"]
standard_ans=["hello","hi"]
chat1=ChatBot(standard_ans,Question_ans)

while True:
    ans = input()
    chat1.reply(ans)


#chat1.learn()
