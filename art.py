import turtle

window = turtle.Screen()
window.bgcolor("black")

def draw_triangle(turtle_name, radius):
    turtle_name.circle(radius,360,3)

def draw_square(turtle_name, radius):
    turtle_name.circle(radius,360,4)

def draw_leaf(turtle):
    base = turtle.pos()
    turtle.circle(100,75)
    turtle.goto(base)
    turtle.circle(-100,75)
    turtle.goto(base)

dave = turtle.Turtle()
dave.shape("turtle")
dave.color("Green", "SeaGreen")

charlie = turtle.Turtle()
charlie.shape("turtle")
charlie.color("Green", "DarkGreen")
charlie.speed(0)

def draw_art(turtle1, turtle2, degrees):
    i = 0
    while i < 360:
        draw_triangle(turtle1, 80)
        draw_square(turtle1, 55)
        turtle1.right(degrees)
        i = i + degrees
        draw_square(turtle1, 70)
        draw_triangle(turtle1, 40)
        turtle1.right(degrees)
        i = i + degrees
    turtle1.ht()
    turtle2.right(90)
    turtle2.forward(400)
    turtle2.left(62)
    draw_leaf(turtle2)
    leaves = 0
    while leaves < 6:
        turtle2.left(27)
        draw_leaf(turtle2)
        leaves = leaves + 1
    turtle2.ht()
    
draw_art(charlie,dave,5)

window.exitonclick()