import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    sq = turtle.Turtle()
    sq.color("yellow")
    sq.speed(10)

    i=1
    while i == 1 :
        for num in range(0, 4):
            sq.forward(200)
            sq.right(90)

        sq.right(15)

    window.exitonclick()

draw_square()