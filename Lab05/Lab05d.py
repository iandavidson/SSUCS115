"""
Program: CS 115 Lab 5d
Author: Ian Davidson
Description: This program draws a graph and identifies mins and maxs giving different colors for each.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)
    # Open the input file and read the number of points
    pointsfile = open("points.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())   # get the first y-coordinate
    first_point = Point(x, window_height - first_y)
    x += 10
    second_y = int(pointsfile.readline())
    second_point = Point(x, window_height - second_y)
    ########## Complete this code: draw the line between these 2 points
    line = Line(first_point, second_point)
    line.setOutline('orange')
    line.draw(window)
    ########## Fix this if-statement
    if second_y > first_y:
        increasing = True
        circle = Circle(first_point, 3)
        circle.setFill("blue")
        circle.draw(window)
        print(first_y, "is a valley.")

    else:
        increasing = False
        circle = Circle(first_point, 3)
        circle.setFill("red")
        circle.draw(window)
        print(first_y, "is a peak.")
    first_y = second_y
    first_point = second_point

    for i in range(2, num_points):  # already did first 2
        x += 10
        second_y = int(pointsfile.readline())
        second_point = Point(x, window_height - second_y)

       ############
       # Copy this code from Part C
       # draw the line between first_point and second_point
       # draw a circle centered at first_point with radius 1
       ############

       ############
        if increasing:
            if (first_y > second_y):
                circle = Circle(first_point, 3)
                circle.setFill("red")
                circle.draw(window)
                print(first_y, "is a peak.")
            else:
                circle = Circle(first_point, 1)
                circle.draw(window)
        elif not increasing:
            if (first_y < second_y):
                circle = Circle(first_point, 3)
                circle.setFill("blue")
                circle.draw(window)
                print(first_y, "is a valley.")
            else:
                circle = Circle(first_point, 1)
                circle.draw(window)
        line = Line(first_point, second_point)
        line.setOutline('orange')
        line.draw(window)
        increasing = second_y > first_y       # second_point becomes the first point of the next line
        first_y = second_y
        first_point = second_point
    if not increasing :
        circle = Circle(first_point, 3)
        circle.setFill("blue")
        circle.draw(window)
        print(first_y, "is a valley.")

    else:
        circle = Circle(first_point, 3)
        circle.setFill("red")
        circle.draw(window)
        print(first_y, "is a peak.")
    ###### Complete this code
    # Decide and print whether first_point is a peak or a valley
    # Draw the appropriate circle

    window.getMouse()
    window.close()
main()