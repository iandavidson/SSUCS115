"""
Program: CS 115 Lab 3b
Author: Ian Davidson
Description: Using the graphics package, this program will draw a circle.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    circle = Circle(Point(100, 200), 40)  # create a circle centered at (100, 200) with radius 40
    circle.setOutline('blue')
    circle.draw(window)              # draw the circle in the window that we created earlier

    window.getMouse()                # wait for the mouse to be clicked in the window
    window.close()                   # close the window after the mouse is clicked in the window


main()
