import turtle

# The Snake class inherits from the Turtle class
class Snake(turtle.Turtle):
    # Constructor
    def __init__(self, headColor, tailColor, xPos, yPos):
        super().__init__()
        self.shape("square")
        self.snakeColor = headColor
        self.tailColor = tailColor
        
        # Add additional properties 
        self.score = 0
        self.position = [xPos, yPos]  # Grid Coordinates on a 20x20 grid
        self.direction = "right"
        self.tail = []
        
    # Redraw the snake head at the right position 
    def draw(self):
        self.clear()
        self.shape("square")
        self.penup()
        self.color(self.snakeColor)
        self.goto(-190 + self.position[0] * 20, 190 - self.position[1] * 20)
        self.stamp()
        
        # Redraw the tail
        for position in self.tail:
            self.color(self.tailColor)
            self.goto(-190 + position[0] * 20, 190 - position[1] * 20)
            self.stamp()
        
        if len(self.tail) >= 1:
            self.tail.append((self.position[0], self.position[1]))
            self.tail.pop(0)
            
    def move(self):
        if self.direction == "up":
            self.position[1] -= 1
        elif self.direction == "down":
            self.position[1] += 1
        elif self.direction == "left":
            self.position[0] -= 1
        elif self.direction == "right":
            self.position[0] += 1

        self.draw()
                
    # Add current position to the tail of the snake to make it grow/extend its tail
    def grow(self):
        self.tail.append((self.position[0], self.position[1]))
                    
    # A method to check if the snake has gone over the edge of the screen
    def isOffScreen(self):
        if self.position[0] < 0 or self.position[0] >= 20 or self.position[1] < 0 or self.position[1] >= 20:
            return True
        return False
    
    # A method to check if the snake is biting its own tail
    def isBitingTail(self):
        for i in range(len(self.tail) - 1):
            if self.position[0] == self.tail[i][0] and self.position[1] == self.tail[i][1]:
                return True
        return False


#Finish