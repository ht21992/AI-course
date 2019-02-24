class student:
    def __init__(self,diligence,responsibility,background):
        self.diligence=diligence
        self.responsibility=responsibility
        self.background=background

def Perdict(student):
    average=(student.diligence+student.responsibility+student.background)/3
    print(average)

s1=student(70,60,75)
Perdict(s1)