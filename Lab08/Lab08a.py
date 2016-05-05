"""
Program: CS 115 Lab 8a
Author: Ian Davidson
Description: This program displays national flags.
"""

from graphics import *

def draw_stripe(window, top_left, bottom_right, color):
    '''
    Draws a rectangle in the window
    Parameters:
    - window: the window to draw in
    - top_left: the coordinates of the top left corner (as a Point)
    - bottom_right: the coordinates of the bottom right corner (as a Point)
    - color: the color to make the rectangle (as a string)

    Returns: nothing
    '''
    stripe = Rectangle(top_left, bottom_right)
    stripe.setFill(color)
    stripe.setOutline(color)
    stripe.draw(window)


def draw_sudan_flag(flag_width):
    '''
    Draws a French flag in the graphics window.
    Parameter: the width of the window
    Returns: nothing
    '''

    flag_height = 1 / 2 * flag_width
    stripe_colors = ['red', 'white', 'black']
    stripe_width = flag_width
    stripe_height = flag_height / len(stripe_colors)

    # Open a new graphics window with the title 'French flag', the
    # width provided by the user, and the calculated height
    window = GraphWin('French flag', flag_width, flag_height)

    # Draw the blue stripe
    # The top left of the stripe is the top left of the window
    # The bottom right of the stripe is 1/3 of the way across
    # the flag, and all the way to the bottom.
    added_y = 0
    for elem in stripe_colors:
        stripe_top_left = Point(0, 0 + added_y)
        stripe_bottom_right = Point(stripe_width, stripe_height + added_y)
        draw_stripe(window, stripe_top_left, stripe_bottom_right, elem)
        added_y += stripe_height
    ######### Write similar code for the white and red stripes.
    triangle = Polygon(Point(0, 0), Point(flag_width/3, flag_height/2), Point(0, flag_height))
    triangle.setFill('DarkGreen')
    triangle.draw(window)
    # Close?
    input('Press ENTER to close the flag window.')
    window.close()

def draw_bangladesh_flag(flag_width):
    ''' Draws the national flag of Japan in a graphics window.

    Parameter: the width of the window
    Returns: nothing
    '''
    flag_height = 3 / 5 * flag_width
    circle_diameter = 2 / 5 * flag_width

    # Open a new graphics window with the title 'Japanese flag',
    # the width passed by the caller, and the calculated height
    win = GraphWin('Bangladesh flag', flag_width, flag_height)

    # Set the window background to white
    win.setBackground('DarkGreen')

    # Set up the red circle.
    circle_center = Point(flag_width * 9 / 20, flag_height / 2)
    circle_radius = circle_diameter / 2

    # Create a circle that is centered in the middle of the flag
    # and has the specified radius
    circ = Circle(circle_center, circle_radius)

    # Turn that circle red
    circ.setFill('red')     # the inside of the circle
    circ.setOutline('red')  # the line around the circle

    # Actually draw the circle
    circ.draw(win)

    # Close?
    input('Press ENTER to close the flag window.')
    win.close()


# --- Our main function ---
def main():
    #draw_bangladesh_flag(600)  # Draw a Japanese flag with a width of 600 pixels
    draw_sudan_flag(600)

main()
