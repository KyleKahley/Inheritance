
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant): # can't create subclass without creating superclass (plant)
    def __init__(self,color, petals):
        Plant.__init__(self,color) #if you skip this you will get an error 

        self.__petals = petals

    def get_petals(self):
        return self.__petals
