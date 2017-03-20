import turtle

# draw square
def draw_square(square):
	for i in range(1,5):
		square.forward(100)
		square.right(90)


#draw art : circle with square
def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	#create Square
	square = turtle.Turtle()
	square.shape("circle")
	square.color("yellow")
	square.speed(20)

	for i in range(1,37):
		draw_square(square)
		square.right(10)
	

	window.exitonclick()

draw_art()
