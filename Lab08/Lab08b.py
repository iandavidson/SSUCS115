"""
Program: CS 115 Lab 8a
Author: Ian Davidson
Description: This program displays national flags.
"""

from graphics import *
import sys

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

def draw_france_flag(flag_width):
    '''
    Draws a French flag in the graphics window.
    Parameter: the width of the window
    Returns: nothing
    '''

    flag_height = 2 / 3 * flag_width
    stripe_colors = ['DarkBlue', 'white', 'red']
    stripe_width = flag_width / len(stripe_colors)

    # Open a new graphics window with the title 'French flag', the
    # width provided by the user, and the calculated height
    window = GraphWin('French flag', flag_width, flag_height)

    # Draw the blue stripe
    # The top left of the stripe is the top left of the window
    added_x = 0
    for elem in stripe_colors:
        blue_stripe_top_left = Point(0 * stripe_width + added_x, 0)

    # The bottom right of the stripe is 1/3 of the way across
    # the flag, and all the way to the bottom.
        blue_stripe_bottom_right = Point(stripe_width + added_x, flag_height)
        draw_stripe(window, blue_stripe_top_left, blue_stripe_bottom_right, elem)
        added_x += flag_width/3
    ######### Write similar code for the white and red stripes.

    # Close?
    input('Press ENTER to close the flag window.')
    window.close()

def draw_russian_flag(flag_width):
    '''
    Draws a French flag in the graphics window.
    Parameter: the width of the window
    Returns: nothing
    '''

    flag_height = 2 / 3 * flag_width
    stripe_colors = ['white', 'blue', 'red']
    stripe_width = flag_width / len(stripe_colors)
    stripe_height = flag_height/3
    # Open a new graphics window with the title 'French flag', the
    # width provided by the user, and the calculated height
    window = GraphWin('Russian flag', flag_width, flag_height)

    # Draw the blue stripe
    # The top left of the stripe is the top left of the window
    added_y = 0
    for elem in stripe_colors:
        blue_stripe_top_left = Point(0, 0 + added_y)
    # The bottom right of the stripe is 1/3 of the way across
    # the flag, and all the way to the bottom.
        blue_stripe_bottom_right = Point(flag_width, stripe_height + added_y)
        draw_stripe(window, blue_stripe_top_left, blue_stripe_bottom_right, elem)
        added_y += stripe_height
    ######### Write similar code for the white and red stripes.

    # Close?
    input('Press ENTER to close the flag window.')
    window.close()


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
    window = GraphWin('Sudan flag', flag_width, flag_height)

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

def draw_japan_flag(flag_width):
    ''' Draws the national flag of Japan in a graphics window.

    Parameter: the width of the window
    Returns: nothing
    '''
    flag_height = 2 / 3 * flag_width
    circle_diameter = 3 / 5 * flag_height

    # Open a new graphics window with the title 'Japanese flag',
    # the width passed by the caller, and the calculated height
    win = GraphWin('Japanese flag', flag_width, flag_height)

    # Set the window background to white
    win.setBackground('white')

    # Set up the red circle.
    flag_center = Point(flag_width / 2, flag_height / 2)
    circle_radius = circle_diameter / 2

    # Create a circle that is centered in the middle of the flag
    # and has the specified radius
    circ = Circle(flag_center, circle_radius)

    # Turn that circle red
    circ.setFill('red')     # the inside of the circle
    circ.setOutline('red')  # the line around the circle

    # Actually draw the circle
    circ.draw(win)

    # Close?
    input('Press ENTER to close the flag window.')
    win.close()


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

    user_width = int(input("Window width: "))
    if 100 < user_width < 1000:

        print("Which national flag(s) do you want to draw?")
        print("- Japan")
        print("- Bangladesh")
        print("- France")
        print("- Russia")
        print("- Sudan")
        which_drawn = input("Name your country: ")
        which_drawn = which_drawn.lower()
        user_list = which_drawn.split()
        for i in range(len(user_list)):
            if user_list[i] == 'japan':
                draw_japan_flag(user_width)
            elif user_list[i] == 'bangladesh':
                draw_bangladesh_flag(user_width)
            elif user_list[i] == 'france':
                draw_france_flag(user_width)
            elif user_list[i] == 'russia':
                draw_russian_flag(user_width)
            elif user_list[i] == 'sudan':
                draw_sudan_flag(user_width)
            else:
                print("Error:", user_list[i], "is not a valid country.")
    else:
        sys.exit("Error: Window size should be between 100 and 1000")
main()
