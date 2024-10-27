# Import turtle package 
import turtle 
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(1280,720)

turtle.title("Welcome to Turtle")

pen = turtle.Turtle() 

pen.left(140) 
pen.forward(113) 
for i in range(200): 
	pen.right(1) 
	pen.forward(1) 
pen.left(120) 
for i in range(200): 
	pen.right(1) 
	pen.forward(1) 
pen.forward(112)  
pen.end_fill() 

