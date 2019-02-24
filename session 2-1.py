class Person:
    def __init__(self,height,weight,hair_legnth):
        self.height=height
        self.weight=weight
        self.hair_legnth=hair_legnth

def Recognize(person):
    if person.height<170 and person.weight<70 and\
            person.hair_legnth>30:
        print("Woman")
    else:
        print("Man")





p1=Person(140,60,40)
p2=Person(190,100,10)
Recognize(p1)
Recognize(p2)