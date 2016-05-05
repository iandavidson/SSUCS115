"""
Program: CS 115 Lab 5b
Author: Ian Davidson
Description: This program draws a line graph, with circles around each point.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("points-test.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())   # get the first y-coordinate
    first_point = Point(x, window_height - first_y)
    # We already have the first point, so start with 1.
    for i in range(1, num_points):
        # Read the next point and update x
        circle = Circle(first_point, 1)
        circle.draw(window)
        second_y = int(pointsfile.readline())
        x += 10
        second_point = Point(x, window_height - second_y)
        line = Line(first_point, second_point)
        line.setOutline('orange')
        line.draw(window)
        ######## COMPLETE THE CODE
        #draw the line between first_point and second_point.
        #draw a circle centered at first_point
        second_point = Point(x, window_height - second_y)
        # use the second point of this line for the first point
        # of the next line
        first_point = second_point
    circle = Circle(first_point, 1)
    circle.draw(window)
    window.getMouse()
    window.close()
main()