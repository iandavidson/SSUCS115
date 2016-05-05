"""
Program: CS 115 Lab 3 Part E
Author: Ian Davidson
Description: Using the graphics package, this program will draw a square of circles, with an 'x' of circles within the
square. Has user input for amount of circles per side and radius of circle.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)
    # 1. Get the number of circles and the radius from the user.
    num_circles = int(input("how many circles?"))
    radius = int(input("radius size?"))
    # 2. Draw the left vertical circles.
    x = radius*2
    y = radius*2
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        y += radius*2
    # 3. Draw the top horizontal circles.
    x = radius*2
    y = radius*2
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        x += radius*2
    # 4. Draw the bottom horizontal circles.
    x = radius*2
    y = (radius*2)+(radius*2*(num_circles-1))
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        x += radius*2
    # 5. Draw the right vertical circles.
    x = (radius*2)+(radius*2*(num_circles-1))
    y = radius*2
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        y += radius*2
    # 6. Draw the top-left-to-bottom-right diagonal circles.
    x = radius*2
    y = radius*2
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)
        y += radius*2
        x += radius*2
    # 7. Draw the top-right-to-bottom-left diagonal circles.
    x = (radius*2)+(radius*2*(num_circles-1))
    y = radius*2
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)
        y += radius*2
        x -= radius*2


    window.getMouse()
    window.close()


main()