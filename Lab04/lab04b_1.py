"""
    Program: CS 115 Lab 4b_1
    Author: Ian Davidson
    Description: This program draws a few rectangles and fills them.
"""
from graphics import *
from random import seed, randint
from time import clock


def random_color():
    # Don't worry about the internal details of this function.
    colors = ['blue', 'blue2', 'blue3',
              'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3',
              'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3',
              'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3',
              'pink', 'pink1', 'pink2', 'pink3']

    return colors[randint(0, len(colors) - 1)]


def main():
    seed()  # Initialize random number generator
    window = GraphWin('Lab 4B', 800, 800)
    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 60

    num_rows = int(input('Number of rows: '))  # commented out for now
    num_columns = int(input('Number of columns: '))
    for i in range(num_columns):
        top_left_point = Point(top_left_x, top_left_y)
        bottom_right_point = Point(top_left_x + width, top_left_y + height)
        enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
        enclosing_rectangle.setFill(random_color())
        enclosing_rectangle.draw(window)
        for k in range(num_rows):
            top_left_point = Point(top_left_x, top_left_y)
            bottom_right_point = Point(top_left_x + width, top_left_y + height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
            enclosing_rectangle.setFill(random_color())
            enclosing_rectangle.draw(window)
            top_left_y += height
        top_left_y -= (height) * (k + 1)
        top_left_x += width
    for i in range(10):
        c_point = window.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
        place_row = ((y_c_point - 100) // width) + 1
        place_columns = ((x_c_point - 100) // height) + 1
        if (100 < x_c_point < 100 + num_columns * width) and (100 < y_c_point < 100 + num_rows * height):
            print('The click at (' + x_c_point + ',', y_c_point + ')', 'is in row',
            place_row + ', column', place_columns + '.')
        else:
            print('The click at (' + x_c_point + ',', y_c_point + ')', 'is outside of the grid.')
    window.getMouse()
    window.close()


main()
