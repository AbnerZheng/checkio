#coding=utf8
__author__ = '璐'

import turtle

def draw_windmill():
    frad = turtle.Turtle("turtle")
    frad.speed(0)
    frad.color("white")

    for i in range(36):
        for j in range(4):
            frad.forward(100)
            frad.right(90)
        frad.right(10)
    frad.right(90)
    frad.forward(300)

def main():
    window = turtle.Screen()
    window.bgcolor("#82B2FF")
    draw_windmill()
    window.exitonclick()

if __name__ == '__main__':
    main()
