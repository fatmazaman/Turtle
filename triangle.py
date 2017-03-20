import turtle

def draw_traingle(triangle, d1, t1, d2, t2, d3, t3):
	triangle.forward(d1)
	triangle.left(t1)
	triangle.forward(d2)
	triangle.left(t2)
	triangle.forward(d3)
	triangle.left(t3)



def draw():
	window = turtle.Screen()
	window.bgcolor("black")


	#create Triangle 
	triangle = turtle.Turtle()
	triangle.shape("turtle")
	triangle.color("red")
	triangle.speed(30)


	
	adding = 0
	while adding < 45 :
		draw_traingle(triangle, 90, 120, 90, 120, 90, 120)
		draw_traingle(triangle, 100, 120, 100, 120, 100, 120)
		draw_traingle(triangle, 90, 140, 12, 140, 90, 1)

		adding += 1		

	window.exitonclick()
draw()
