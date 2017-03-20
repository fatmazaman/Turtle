import turtle

def draw_square(square, d1, t1, d2, t2, d3, t3, d4, t4):
	square.forward(d1)
	square.left(t1)
	square.forward(d2)
	square.left(t2)
	square.forward(d3)
	square.left(t3)
	square.forward(d4)
	square.left(t4)



def draw():
	window = turtle.Screen()
	window.bgcolor("black")

	#create Square
	square = turtle.Turtle()
	square.shape("circle")
	square.color("blue")
	square.speed(100)

	
	adding = 0
	while adding < 180 :
	
		draw_square(square, 100, 90, 100, 90, 100, 90, 100, 90)
		draw_square(square, 100, 300, 100, 90, 100, 90, 100, 90)
		draw_square(square, 100, 300, 100, 90, 100, 90, 100, 90)
		draw_square(square, 100, 300, 100, 90, 100, 90, 100, 1)

		adding += 1		

	window.exitonclick()
draw()
