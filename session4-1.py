import numpy
class GoToWalkANN:
    def __init__(self,the_weather=1.0,the_mood=1.0,the_friends=1.0):
        self.weather=the_weather
        self.mood=the_mood
        self.friends=the_friends
    def activationFunction(self,x):
        if x>=0.5:
            return 1
        else:
            return 0


    def solve(self):
        inputs=numpy.array([self.weather,self.mood,self.friends])
        weightsInputToHidden1=[9,5,1]
        weightsInputToHidden2 = [7, 2, 10]
        weightsInputToHidden= numpy.array([weightsInputToHidden1,weightsInputToHidden2])
        weightsHidenToOutput=numpy.array([-1,1])

        hiddenInput=numpy.dot(weightsInputToHidden,inputs)
        print("hidden input "+ str(hiddenInput))

        hiddenoutput=numpy.array([self.activationFunction(x) for x in hiddenInput])
        print("hidden output: "+ str(hiddenoutput))

        ouput=numpy.dot(weightsHidenToOutput,hiddenoutput)
        print("output :"+ str(ouput))
        return self.activationFunction(ouput)


somenuralnetwork=GoToWalkANN()
print("result : " +str(somenuralnetwork.solve()))
        