import turtle

def drawFractalTriangle(aTurtle, depth, maxdepth):
    if depth > maxdepth:
        return
    else:
        for i in range(3):
            aTurtle.forward(256/(2**depth))
            drawFractalTriangle(aTurtle, depth+1, maxdepth)
            aTurtle.forward(256/(2**depth))
            aTurtle.left(120)
        return

def draw_picture():
    window = turtle.Screen()
    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('blue')
    brad.penup()
    brad.goto(-50, -200)
    brad.pendown()
    brad.speed(0)
    brad.right(180)
    brad.forward(256)
    brad.right(180)
    drawFractalTriangle(brad, 0, 4)
    window.exitonclick()

draw_picture()