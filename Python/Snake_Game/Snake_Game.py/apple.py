import turtle
import random

#The Apple class intherit from the Turtle class!
class Apple(turtle.Turtle):
    #Constructor 
    def __init__(self,color,xPos,yPos):
        #Call the parent constructor to initialise the Snake as a Turtle!
        super().__init__()
        self.shape("circle")
        self.appleColor = color
        
        #Add additional properties using random grid coordinates
        self.position = [xPos,yPos] #Grid Coordinates
        
    def draw(self):
        self.clear()
        self.shape("circle")
        self.penup()
        self.color(self.appleColor)
        self.hideturtle()
        self.goto(-190 + self.position[0]*20, 190 - self.position[1]*20)
        self.stamp()
        
    def respawn(self):
        self.position = [random.randint(0,19),random.randint(0,19)]
        self.draw()