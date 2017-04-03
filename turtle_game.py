import turtle

my_turtle=turtle.Turtle()
def square(length, angle):
            
            my_turtle.forward(length)
            my_turtle.left(angle)
            my_turtle.forward(length)
            my_turtle.left(angle)
            my_turtle.forward(length)
            my_turtle.left(angle)
            my_turtle.forward(length)

for i in range(10):
    square(50,90)
    my_turtle.forward(100)
    square(100,90)
