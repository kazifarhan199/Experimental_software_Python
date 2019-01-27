import turtle
import random

points = 0

def Check():
	#Using global will allow us to change points 
	global points

	#Asking for location of snake 
	snakeX, snakeY = snake.position()

	#Asking for location of food	
	foodX, foodY = food.position()

	#checking if Snake ate the food
	if (snakeX >= foodX-20 and snakeX <= foodX+20) and (snakeY >= foodY-20 and snakeY <= foodY+20):
		#Placing food on other  location
		PlaceFood()
		#increasing the score
		points+=1
		#Clearing and re-writing the Score
		score.clear()
		score.write("Score : "+str(points), font=(None,20))

	#Checking if snake went out of the width of the boundary
	if snakeX >= 235  or snakeX <= -235:
		snake.goto(0,0)
		#Checking if turtle ate food as food can be at (0, 0)
		Check()
		#As snake went out of the boundary points = 0
		points=0
		#Clearing and re-writing the Score
		score.clear()
		score.write("Score : "+str(points), font=(None,20))

	#Checking if snake went out of the height of the boundary
	if snakeY >= 235 or snakeY <= -235:
		snake.goto(0,0)
		#Checking if turtle ate food as food can be at (0, 0)
		Check()
		#As snake went out of the boundary points = 0
		points=0
		#Clearing and re-writing the Score
		score.clear()
		score.write("Score : "+str(points), font=(None,20))

def PlaceFood():
	#Place food at random location in the boundary
	foodX = random.randrange(-200,200)
	foodY = random.randrange(-200, 200)
	food.goto(foodX, foodY)

def moveRight():
	#Defining What to happen when right is pressed
	snake.right(90)

def moveLeft():
	#Defining What to happen when left is pressed
	snake.left(90)

def moveUp():
	#Defining What to happen when up is pressed
	snake.forward(40)
	#Check if snake is inside the boundary and if he ate food
	Check()

def moveDown():
	#Defining What to happen when down is pressed
	snake.back(80)
	#Check if snake is inside the boundary and if he ate food
	Check()

def CreateBoundary():
	#Creating a new pen
	boundary = turtle.Turtle()
	boundary.penup()
	boundary.speed(0)
	
	#Placing it on 250, -250
	boundary.goto(250,-250)
	
	#Drawing usein pen
	boundary.pendown()
	
	#Hiding the pen tip
	boundary.hideturtle()
	
	#Creating  a Square 
	for i in range(5):
		boundary.back(500)
		boundary.right(90)

def BindButtons():
	#Defining which function should be callsed if we give input
	myscreen.onkeypress(moveRight, "Right")
	myscreen.onkeypress(moveLeft, "Left")
	myscreen.onkeypress(moveUp, "Up")
	myscreen.onkeypress(moveDown, "Down")

#Usin this if Statement so that the code only runs when this file is run
if __name__ == "__main__":
	
	#Initilize the Screen/Window
	myscreen = turtle.Screen()
	myscreen.title("Snake Game")

	#Defining what will happen if different button is pressed
	BindButtons()
	
	#Listen for any button press
	myscreen.listen()

	#Create a Square Boundary For Game
	CreateBoundary()

	#Create The main Turtle
	snake = turtle.Turtle()
	snake.shape("turtle")
	snake.penup()

	#Create Food
	food = turtle.Turtle()
	food.shape("circle")
	food.penup()
	food.speed(0)
	
	#Place food at random location inside the screen 
	PlaceFood()

	#Write Score on top right hand side outside the boundary 
	score = turtle.Turtle()
	score.penup()
	score.goto(200, 260)
	score.pendown()
	score.write("Score : 0",font=(None,20))
	score.hideturtle()

	#Don't close the window till we close it
	turtle.done()