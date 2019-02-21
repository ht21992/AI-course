import random
import time
class ChatBot:
    def __init__(self,standardanswer,questionanswer,greetinganswer,farewellanswer):
        self.standardanswer=standardanswer
        self.questionanswer=questionanswer
        self.greetinganswer=greetinganswer
        self.farewellanswer=farewellanswer
    def check_greeting(self,text):
        text=text.lower()
        for greeting in self.greetinganswer:
            if text.__contains__(greeting):
                return True
    def check_farewell(self,text):
        text=text.lower()
        for farewell in self.farewellanswer:
            if text.__contains__(farewell):
                return True
    def reply(self,text):
        if self.check_farewell(text):
            random_ans = random.randint(0, len(self.farewellanswer) - 1)
            print(self.farewellanswer[random_ans])
            exit()
        elif self.check_greeting(text):
            random_ans = random.randint(0, len(self.greetinganswer) - 1)
            print(self.greetinganswer[random_ans])
        elif "?" in text:
            random_ans=random.randint(0,len(self.questionanswer)-1)
            print(self.questionanswer[random_ans])
        else:
            random_ans=random.randint(0,len(self.standardanswer)-1)
            print(self.standardanswer[random_ans])
    def learn(self,text):
        if "?" in text:
            self.questionanswer.append(text)
        else:
            self.standardanswer.append(text)



Greetings=["hello","hi","greetings","sup","what's up"]
Farewells=["bye","talk to you later","see you later","goodbye"]
Question_ans=["who knows","i do know the answer"]
standard_ans=["that's good","so sad","intersting"]
chat1=ChatBot(standard_ans,Question_ans,Greetings,Farewells)
chat1.learn("sound's good")

while True:
    ans = input()
    chat1.reply(ans)
