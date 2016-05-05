"""
Program: CS 115 Lab 3 Part D
Author: Ian Davidson
Description: Using the graphics package, this program will draw a number of
             circles stacked on one another using a for-loop. includes user input of radius and number of circles
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    x = 100
    y = 100
    num_circles = int(input("how many circles?"))
    radius = int(input("radius size?"))
    for i in range(num_circles):
        print('x =', x, 'and y =', y)
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('DarkGoldenrod3')
        circle.draw(window)
        y += radius*2

    window.getMouse()
    window.close()


main()
