import turtle

def draw_turtle():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	brad.speed(2)

	for i in range (4):
		brad.forward(100)
		brad.right(90)

	window.exitonclick()

draw_turtle()