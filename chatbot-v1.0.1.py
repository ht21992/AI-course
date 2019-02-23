import random
class Bot:
    bot_knowledge={"greetings":["hello","hi","greetings","sup","what's up"],"farewells":["bye","talk to you later","see you later","goodbye"]
    ,"mood":["how are you","how is it going","how are you today"],"Soccer":["Football","Barcelona","Chelsea","Real Madrid","Arsenal"],
    "Movie":["cinema","gone with the wind","movie"],
    "Food":["Food","Burger","pizza","pasta","lunch","dinner","supper","susage","breakfast"]}
    def __init__(self,movie_ans,soccer_ans,food_ans,standardanswer,questionanswer):
        self.movie_ans=movie_ans
        self.soccer_ans=soccer_ans
        self.food_ans=food_ans
        self.standardanswer = standardanswer
        self.questionanswer = questionanswer
    def check_greeting(self, text):
        text = text.lower()
        for greeting in Bot.bot_knowledge["greetings"]:
            if text.__contains__(greeting):
                return True
    def check_farewell(self, text):
        text = text.lower()
        for farewell in Bot.bot_knowledge["farewells"]:
            if text.__contains__(farewell):
                return True
    def check_movie(self,text):
        text=text.lower()
        if "cinema" in text or text=="cinema":
            return "cinema"
        for knowledge in Bot.bot_knowledge["Movie"]:
            if text.__contains__(knowledge) :
                return True
    def check_food(self,text):
        text = text.lower()
        for food in Bot.bot_knowledge["Food"]:
            if text.__contains__(food) :
                return True
    def check_soccer(self,text):
        text=text.lower()
        for soccer in Bot.bot_knowledge["Soccer"]:
            if text.__contains__(soccer) :
                return True
    def check_mood(self,text):
        text.lower()
        for mood in Bot.bot_knowledge["mood"]:
            if text.__contains__(mood):
                return True
    def reply(self, text):
        if self.check_farewell(text):
            random_ans = random.randint(0, len(Bot.bot_knowledge["farewells"]) - 1)
            print(Bot.bot_knowledge["farewells"][random_ans])
            exit()
        elif self.check_greeting(text):
            random_ans = random.randint(0, len(Bot.bot_knowledge["greetings"]) - 1)
            print(Bot.bot_knowledge["greetings"][random_ans])
        elif self.check_mood(text):
            print("not bad")
        elif self.check_movie(text)=="cinema":
            cinema_ans=list(filter(lambda x:"cinema" in x,self.movie_ans))
            print(random.choice(cinema_ans))
        elif self.check_movie(text):
            movie = list(filter(lambda x: "movie" in x, self.movie_ans))
            print(random.choice(movie))
        elif self.check_food(text):
            random_ans = random.randint(0, len(self.food_ans) - 1)
            print(self.food_ans[random_ans])
        elif self.check_soccer(text):
            random_ans= random.randint(0, len(self.soccer_ans) - 1)
            print(self.soocer_ans[random_ans])
        elif "?" in text:
            random_ans=random.randint(0,len(self.questionanswer)-1)
            print(self.questionanswer[random_ans])
        else:
            random_ans=random.randint(0,len(self.standardanswer)-1)
            print(self.standardanswer[random_ans])
    def learn(self, text):
        if "?" in text:
            self.questionanswer.append(text)
        else:
            self.standardanswer.append(text)

Movie_ans=["i watch at least one movie each week","i like Perfume movie","usually i don't go to cinema","cinema,huumm... no"]
Soccer_ans=["football is awsome","i am a chelsea fan","i watch Preimer League","i don't like La Liga"]
Food_ans=["i like pizza","i almost eat everything","i like burger"]
Question_ans=["who knows","i do know the answer"]
standard_ans=["that's good","i see","intersting","ok"]
chat1=Bot(Movie_ans,Soccer_ans,Food_ans,standard_ans,Question_ans)
chat1.learn("sound's good")
while True:
    ans = input()
    chat1.reply(ans)
