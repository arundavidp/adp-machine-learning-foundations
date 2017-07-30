import turtle

def draw_circle_sqaures(new_turtle, angle):
	draw_angle = angle
	draw_square(new_turtle)
	print new_turtle.heading()
	while (draw_angle % 360 != 0):
		new_turtle.setheading(draw_angle)
		draw_square(new_turtle)
		print new_turtle.heading()
		draw_angle = new_turtle.heading() + angle


def draw_square(new_turtle):
	for i in range (4):
		new_turtle.forward(100)
		new_turtle.right(90)

def draw_turtle():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	brad.speed(2)

	draw_circle_sqaures(brad, 390)

	window.exitonclick()

draw_turtle()