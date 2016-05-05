"""
    Program: CS 115 Lab 4a_1
    Author: Ian Davidson.
    Description: This program uses the graphics package
        to interact with the user.
"""
from graphics import *


def main():
    window = GraphWin('Lab 4a_1', 400, 600)
    radius = 20
    for i in range(5):
        click_point = window.getMouse()
        click_point_x = click_point.getX()
        click_point_y = click_point.getY()
        center = Point(click_point_x, click_point_y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)
        print('x = ', click_point_x, ', y = ', click_point_y, sep="")
    window.getMouse()
    window.close()

main()