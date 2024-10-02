import turtle
import random
import time

# Asegúrate de que estas clases estén definidas antes de este punto
from snake import Snake
from apple import Apple

def displayInstructions():
    print("~~~~~~~~~~~~~~~~~~~~")
    print("~                  ~")
    print("~    Snake Game    ~")
    print("~~~~~~~~~~~~~~~~~~~~")
    print("")

def drawBorders():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(7)
    pen.color("#ffffff")
    pen.pensize(2)
    pen.penup()
    pen.goto(-150, -150)
    pen.pendown()
    for _ in range(4):
        pen.forward(300)
        pen.left(90)

# >>> Setup the Stage
screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(333, 333)

# >>> Draw the white borders
drawBorders()

# >>> Add the apple
apple = Apple("#FF0000", random.randint(0, 19), random.randint(0, 19))  
apple.draw()

# >>> Add the Snake...
snake = Snake("#810081", "#B130B1", 0, 19)  # Purple Snake in the bottom left corner (0,0) of the 20x20 grid
snake.direction = "right"
snake.draw()

# >>> Display instructions on how to play the game
displayInstructions()

# Define the maximum score
max_score = 10  # Establece el puntaje máximo

def startGame(x, y):
    global gameOver
    if not gameOver:
        score = 0 
        delay = 0.25
        print(">>> Starting Game")

        while not gameOver:
            screen.bgcolor(200 / 255, 200 / 255, 200 / 255)
            snake.move()

            if snake.isOffScreen():
                print(">>> Game Over! <<<")
                gameOver = True
            elif snake.isBitingTail():
                print(">>> Game Over! <<<")
                gameOver = True
            elif snake.position[0] == apple.position[0] and snake.position[1] == apple.position[1]:
                snake.score += 1
                print("Score: " + str(snake.score) + " pts")
                snake.grow()
                apple.respawn()

            # Verificar si se ha alcanzado el puntaje máximo
            if snake.score >= max_score:
                print(f"Congratulations! You reached the maximum score of {max_score}.")
                gameOver = True

            screen.update()
            time.sleep(delay)

# >>> Implementing motion of the snake in all 4 directions
def go_up():
    if snake.direction != "down":  # Prevents reversing direction directly
        snake.direction = "up"

def go_down():
    if snake.direction != "up":  # Prevents reversing direction directly
        snake.direction = "down"

def go_right():
    if snake.direction != "left":  # Prevents reversing direction directly
        snake.direction = "right"

def go_left():
    if snake.direction != "right":  # Prevents reversing direction directly
        snake.direction = "left"
    
# >>> Keyboard bindings (using the arrow keys)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

# The game will only start once the player clicks on the screen
screen.onscreenclick(startGame, 1)

gameOver = False
screen.mainloop()
