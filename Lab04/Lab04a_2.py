"""
    Program: CS 115 Lab 4a_2
    Author: Ian Davidson
    Description: This program draw a few rectangles and fills them. Later tells user's x and y of click also if it
    is in a box
"""
from graphics import *


def main():
    window = GraphWin('Lab 4a_2', 400, 600)

    yellow_palette_top_left_x = 10
    yellow_palette_top_left_y = 20
    width = 60
    height = 60
    yellow_top_left = Point(yellow_palette_top_left_x, yellow_palette_top_left_y)
    yellow_bottom_right = Point(yellow_palette_top_left_x + width, yellow_palette_top_left_y + height)
    yellow_rectangle = Rectangle(yellow_top_left, yellow_bottom_right)
    yellow_rectangle.setFill('yellow')
    yellow_rectangle.draw(window)

    pink_palette_top_left_x = 70
    pink_palette_top_left_y = 20
    pink_top_left = Point(pink_palette_top_left_x, pink_palette_top_left_y)
    pink_bottom_right = Point(pink_palette_top_left_x + width, pink_palette_top_left_y + height)
    pink_rectangle = Rectangle(pink_top_left, pink_bottom_right)
    pink_rectangle.setFill('pink')
    pink_rectangle.draw(window)

    blue_palette_top_left_x = 130
    blue_palette_top_left_y = 20
    blue_top_left = Point(blue_palette_top_left_x, blue_palette_top_left_y)
    blue_bottom_right = Point(blue_palette_top_left_x + width, blue_palette_top_left_y + height)
    blue_rectangle = Rectangle(blue_top_left, blue_bottom_right)
    blue_rectangle.setFill('blue')
    blue_rectangle.draw(window)

    for i in range(5):
        c_point = window.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
            #yellow
        if (yellow_top_left.getX() <= x_c_point <= yellow_bottom_right.getX() and
            yellow_top_left.getY() <= y_c_point <= yellow_bottom_right.getY()):
            print('The click with x =', c_point.getX(), 'and y =',
                  c_point.getY(), 'is in the yellow square.')
            #pink
        elif (pink_top_left.getX() <= x_c_point <= pink_bottom_right.getX() and
            pink_top_left.getY() <= y_c_point <= pink_bottom_right.getY()):
            print('The click with x =', c_point.getX(), 'and y =',
                  c_point.getY(), 'is in the pink square.')
            #blue
        elif (blue_top_left.getX() <= x_c_point <= blue_bottom_right.getX() and
            blue_top_left.getY() <= y_c_point <= blue_bottom_right.getY()):
            print('The click with x =', c_point.getX(), 'and y =',
                  c_point.getY(), 'is in the blue square.')
        else: print('The click with x =', c_point.getX(), 'and y =',
                  c_point.getY(), 'is not in any square.')

    window.getMouse()
    window.close()
main()