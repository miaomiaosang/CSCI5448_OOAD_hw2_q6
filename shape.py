#from displayer import *

class Shape(object):
    def __init__(self,order,x_location,y_location):
        self.order = order
        self.x_location = x_location
        self.y_location = y_location

    def getX(self):
        return self.x_location

    def getY(self):
        return self.y_location

    def getOrder(self):
        return self.order
        
