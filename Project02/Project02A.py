'''
Assignment: Project2b
Author: Ian Davidson
Description: Display the game window of Mastermind, making circles using loops, and functions
'''
import sys
from graphics import *
from graphicsPlus import *
import random
import math

g_window_width = 360
g_window_height = 700
leftmost_x = 65
palette_y = g_window_height - 50
circle_radius = 20
circle_diameter = 2 * circle_radius
p_circle_spacing = 5
h_circle_spacing = 10
exit_x = 10 + circle_radius
exit_y = 30
state_x = g_window_width - circle_radius
state_y = exit_y
circle_width = 1
guess_y = palette_y - 100
guess_x = leftmost_x + circle_radius + 5
feedback_circle_radius = 5
feedback_x = leftmost_x + 5 * circle_radius * 2 + 4 * h_circle_spacing + feedback_circle_radius
feedback_y = guess_y + circle_radius - feedback_circle_radius
feedback_h_spacing = 20
feedback_v_spacing = 20
secret_code_x = guess_x
secret_code_y = 100
dy = circle_diameter + h_circle_spacing
textbox_x = 180
textbox_y = exit_y
text_size = 30
initial_state_circle_fill = 'white'


def create_exit_circle(win):
    exit_coordinate = Point(exit_x, exit_y)
    exit_circle = Circle(exit_coordinate, circle_radius)
    exit_circle.setFill('red')
    exit_circle.draw(win)
    return exit_circle
    # Using the (exit_x, exit_y) and circle_radius, creates a circle,
    # set its fill-color to red, displays it in "win", and returns it.


def create_state_circle(win):
    state_x = g_window_width - circle_radius
    state_y = exit_y
    state_coordinates = Point(state_x, state_y)
    state_circle = Circle(state_coordinates, circle_radius)
    state_circle.setFill(initial_state_circle_fill)
    state_circle.draw(win)
    return state_circle


def create_palette_circle(win, palette_colors, num_colors):
    palette_circles = []
    offset_x = 0
    for i in range(num_colors):
        palette_point = Point((leftmost_x + offset_x), palette_y)
        palette_circle = Circle(palette_point, circle_radius)
        palette_circle.setFill(palette_colors[i])
        palette_circle.draw(win)
        palette_circles.append(palette_circle)
        offset_x += circle_radius*2 + p_circle_spacing
    return palette_circles


def create_guess_circles(win):
    # set list for circle
    add_guess_x = 0
    guess_circle_LR = []
    for i in range(4):
        guess_coordinates = Point((guess_x + add_guess_x), guess_y)
        circle = Circle(guess_coordinates, circle_radius)
        circle.draw(win)
        guess_circle_LR.append(circle)
        add_guess_x += circle_radius * 2 + p_circle_spacing
    return guess_circle_LR
    # set movement after drawing, make circles left to right


def create_secret_code_colors(palette_colors):
    secret_code_colors = []
    for i in range(4):
        secret_code_colors.append(random.choice(palette_colors))
    return secret_code_colors


def create_secret_code_circles(win, secret_code_colors):
    add_sec_x = 0
    for i in range(4):
        secret_circle_coor = Point((secret_code_x + add_sec_x), secret_code_y)
        circle = Circle(secret_circle_coor, circle_radius)
        circle.setFill(secret_code_colors[i])
        circle.draw(win)
        add_sec_x += circle_radius * 2 + p_circle_spacing

        # The function creates a list of four circles using the colors in secret_code_colors
        # and displays it in "win". The color of the first circle is "secret_code_color[0]"
        # and its center is at (secret_code_x, secret_code_y)


def is_click_in_circle(clickpoint, circle):
    center = circle.getCenter()
    radius = circle.getRadius()
    click_x = clickpoint.getX()
    click_y = clickpoint.getY()
    dist = math.sqrt((click_x - center.x )**2+(click_y - center.y)**2)
    if dist < radius:
        return True
    else:
        return False


def find_clicked_circle(clickpoint, list_of_cirlces):
    for i in range(len(list_of_cirlces)):
        if is_click_in_circle(clickpoint, list_of_cirlces[i]):
            return i
    return None


def move_circles_up(circles):
    for circle in circles:
        circle.move(0, -dy)


    """
    It moves each object in "circles" up by "dy" pixels.

    circles: a list of circles that are already drawn in the graphics window.
    dy: a positive integer. Each circle in "circles" will be moved UP by this number of pixels.
    """


def create_and_display_final_text(text_to_use, win):
    textbox_coor = Point(textbox_x, textbox_y)
    textbox = Text(textbox_coor, text_to_use)
    textbox.setTextColor('orange')
    textbox.setSize(text_size)
    textbox.draw(win)

    """
    Creates a Text-box, sets its text to ‘‘text_to_use’’, its anchor-point at
    (final_text_x, final_text_y), and displays it in the window.
    text_to_use: the text for the Text-box to be created
    win: the graphics window into which the text should be displayed
    return value: None
    """


def guess_is_right(secret_code_colors, guess_colors):
    for i in range(len(secret_code_colors)):
        if secret_code_colors[i] != guess_colors[i]:
            return False
    return True



"""
    Returns True if the corresponding elements of secret_code_colors and guess_colors match.

    secret_code_colors: a list of colors
    guess_colors: a list of color where len(secret_code_colors) == len(guess_colors) is true
    return value: True if all the corresponding elements of the two lists are equal. Otherwise, the function returns False
    """


def main():
    palette_colors = ['green', 'orange', 'darkblue', 'yellow', 'darkred', 'lightblue']
    num_palette_colors = len(palette_colors)
    g_window = GraphWin("Mastermind", g_window_width, g_window_height)
    exit_circle = create_exit_circle(g_window)
    state_circle = create_state_circle(g_window)
    palette_circle_list = create_palette_circle(g_window, palette_colors, num_palette_colors)
    guess_circle_list = create_guess_circles(g_window)
    secret_code_list = create_secret_code_colors(palette_colors)
    secret_circles = create_secret_code_circles(g_window, secret_code_list)
    current_guess_circle_list = [None, None, None, None]
    tries = 1
    exit_circle_clicked = False
    guessing_is_done = False



    while not exit_circle_clicked:
        clickpoint = g_window.getMouse()
        if is_click_in_circle(clickpoint, exit_circle):
            exit_circle_clicked = True
        elif guessing_is_done:
            pass
        else:
            clicked_index_p = find_clicked_circle(clickpoint, palette_circle_list)
            if not clicked_index_p == None:
                state_circle.setFill(palette_circle_list[clicked_index_p].getFill())
            else:
                clicked_index_g = find_clicked_circle(clickpoint, guess_circle_list)
                if not clicked_index_g == None and state_circle.getFill() != initial_state_circle_fill:
                    clicked_circle = guess_circle_list[clicked_index_g]
                    new_circle = clicked_circle.clone() # make a copy of it.
                    new_circle.setFill(state_circle.getFill())
                    new_circle.draw(g_window)
                    current_guess_circle_list[clicked_index_g] = new_circle
                    state_circle.setFill(initial_state_circle_fill)
                    if not None in current_guess_circle_list:
                        tries += 1
                        if tries <= 8:
                            move_circles_up(guess_circle_list)
                            current_guess_circle_list = [None, None, None, None]
                        else:
                            create_and_display_final_text("Done!", g_window)
                            guessing_is_done = True
                else:
                    state_circle.setFill(initial_state_circle_fill)
    sys.exit()

main()