import turtle
angle=95
my_turtle=turtle.Turtle()
def square(length,angle):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)

for i in range(36):
    square(65,90)
    my_turtle.right(angle+5)
    
