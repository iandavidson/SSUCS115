'''
Assignment: Project2b
Author: Ian Davidson
Description: Display the game window of Mastermind, making circles using loops, and functions. The game has the user
select a color then input to a set of guesses. The program tests if the user choices is correct then gives feedback as
a hint. If the code is guessed correctly then the game ends, game also ends if the user takes 8 turns of unsuccessful
guessing.
'''
import sys
from graphics import *
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
'''
    Using the (exit_x, exit_y) and circle_radius, creates a circle,
    set its fill-color to red, displays it in "win", and returns it.
    '''

def create_state_circle(win):
    state_x = g_window_width - circle_radius
    state_y = exit_y
    state_coordinates = Point(state_x, state_y)
    state_circle = Circle(state_coordinates, circle_radius)
    state_circle.setFill(initial_state_circle_fill)
    state_circle.draw(win)
    return state_circle
'''
     Using the (state_x, state_y) and circle_radius, creates a circle,
     displays it in "win", and returns it.
'''


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
'''
    First creates an empty list, then using an accumulator and for loop, 6 circles are created, drawn, then added to
    list. The list of circles is then returned.
    '''


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
'''
    set movement after drawing, drawing circles left to right. each circle is later added to a list then returned.
    '''

def create_secret_code_colors(palette_colors):
    secret_code_colors = []
    for i in range(4):
        secret_code_colors.append(random.choice(palette_colors))
    return secret_code_colors
'''
    using the list of colors, palette_colors, a random 4 code pattern of colors is made.
    '''


def create_secret_code_circles(win, secret_code_colors):
    add_sec_x = 0
    for i in range(4):
        secret_circle_coor = Point((secret_code_x + add_sec_x), secret_code_y)
        circle = Circle(secret_circle_coor, circle_radius)
        circle.setFill(secret_code_colors[i])
        circle.draw(win)
        add_sec_x += circle_radius * 2 + p_circle_spacing
        '''
         The function creates a list of four circles using the colors in secret_code_colors
         and displays it in "win". The color of the first circle is "secret_code_color[0]"
         and its center is at (secret_code_x, secret_code_y)
        '''

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
'''
    takes parameters clickpoint and circle. gets information from the circle and checks if the click is inside the
    circle. If the click is inside then it returns true.
    '''

def find_clicked_circle(clickpoint, list_of_cirlces):
    for i in range(len(list_of_cirlces)):
        if is_click_in_circle(clickpoint, list_of_cirlces[i]):
            return i
    return None
'''
iterates through the list of circles, checking if the click is inside of each. If click is inside a circle the index,
number of the circle in the list is returned.
'''

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


def guess_is_right(secret_code_colors, guess_color_list):
    for i in range(len(secret_code_colors)):
        if secret_code_colors[i] != guess_color_list[i]:
            return False
    return True



"""
    Returns True if the corresponding elements of secret_code_colors and guess_colors match.

    secret_code_colors: a list of colors
    guess_colors: a list of color where len(secret_code_colors) == len(guess_colors) is true
    return value: True if all the corresponding elements of the two lists are equal. Otherwise, the function returns False
    """


def create_feedback_skel():
    #order in list is BotLeft, BotRight, TopLeft, TopRight
    feedback_skel_circles = []
    for v in range(2):
        for h in range(2):
            feedback_coor = Point((feedback_x + feedback_h_spacing*h), feedback_y - feedback_v_spacing*v)
            feedback_circle = Circle(feedback_coor, feedback_circle_radius)
            feedback_skel_circles.append(feedback_circle)
    return feedback_skel_circles
"""
Creates four smaller circles such that when drawn, they form two rows each of which includes 2 circles.
This function will use the variables feedback_x, feedback_y, feedback_h_spacing and feedback_v_spacing
to represent the center of circles and variable feedback_circle_radius for the radius of the circle.
Note this function does not draw the circles.

return value: a list of four circles
"""


def create_feedback_circles(secret_code_colors, guess_code_colors, feedback_skel_circles):

    feedback_circles = []
    guess_color_used = [False, False, False, False]
    secret_color_used = [False, False, False, False]
    feedback_idx = 0
    for match in range(4):
        if secret_code_colors[match] == guess_code_colors[match]:
            guess_color_used[match] = secret_color_used[match] = True
            c = feedback_skel_circles[feedback_idx].clone()
            feedback_idx += 1
            c.setFill('red')
            feedback_circles.append(c)
    for i in range(4):
        if not guess_color_used[i]:
            for j in range(4):
                if not secret_color_used[j] and secret_code_colors[j] == guess_code_colors[i]:
                    c = feedback_skel_circles[feedback_idx].clone()
                    c.setFill('white')
                    feedback_circles.append(c)
                    feedback_idx += 1
                    secret_color_used[j] = True
                    break


    return feedback_circles
"""
Compares secret_code_colors and guess_code_colors and based on the outcome, it creates zero to four circles.

secret_code_colors: a list of 4 colors that represent the secret code
guess_code_colors: a list of 4 colors that represent the code-breaker’s guess
feedback_skel_circles: a list of 4 circles to be used as a model to create feedback circles. For example, if the guess colors were to give rise to two feedback circles, this function clones the first two circles in feedback_skel_circles, "color" them appropriately, and returns them. The original feedback_skel_circles will not be modified in any way by this function.

return value: a list of as few as 0 and as many as 4 circles.
"""

def draw_feedback_list(feedback_circles, win):
    for elem in range(len(feedback_circles)):
            feedback_circles[elem].draw(win)
'''
takes a list of feedback circles and draws them to window
'''

def main():
    palette_colors = ['green', 'orange', 'darkblue', 'yellow', 'darkred', 'lightblue']
    num_palette_colors = len(palette_colors)
    g_window = GraphWin("Mastermind", g_window_width, g_window_height)
    exit_circle = create_exit_circle(g_window)
    state_circle = create_state_circle(g_window)
    palette_circle_list = create_palette_circle(g_window, palette_colors, num_palette_colors)
    guess_circle_list = create_guess_circles(g_window)
    secret_code_list = create_secret_code_colors(palette_colors)
    create_secret_code_circles(g_window, secret_code_list)
    feedback_skel_list = create_feedback_skel()
    current_guess_circle_list = [None, None, None, None]
    tries = 1
    exit_circle_clicked = False
    guessing_is_done = False
    win_response =  'You Win!'
    lose_response = 'You Lose!'
    guess_color_list = [None, None, None, None]
    state_color = None

    while not exit_circle_clicked:
        clickpoint = g_window.getMouse()
        if is_click_in_circle(clickpoint, exit_circle): #checks if clickpoint is inside exit circle
            exit_circle_clicked = True
        elif guessing_is_done:
            pass
        else:
            clicked_index_p = find_clicked_circle(clickpoint, palette_circle_list)
            if not clicked_index_p == None:
                state_color = palette_colors[clicked_index_p]
                state_circle.setFill(state_color)
            else:
                clicked_index_g = find_clicked_circle(clickpoint, guess_circle_list)
                if not clicked_index_g == None and state_color != initial_state_circle_fill:
                    clicked_circle = guess_circle_list[clicked_index_g]
                    new_circle = clicked_circle.clone() # makes a copy of it's location, etc
                    new_circle.setFill(state_color)
                    new_circle.draw(g_window)
                    current_guess_circle_list[clicked_index_g] = new_circle
                    guess_color_list[clicked_index_g] = state_color
                    state_circle.setFill(initial_state_circle_fill)
                    state_color = initial_state_circle_fill
                    if not None in current_guess_circle_list:
                        #check & feedback functions used here
                        feedback_list = create_feedback_circles(secret_code_list, guess_color_list, feedback_skel_list)
                        draw_feedback_list(feedback_list, g_window)
                        if guess_is_right(secret_code_list, guess_color_list):  #checks if guess  is right then ends game
                            create_and_display_final_text(win_response, g_window)
                            guessing_is_done = True
                        else:
                            tries += 1
                            if tries <= 8 and not guessing_is_done: #makes sure there isn't more than 8 tries
                                move_circles_up(guess_circle_list)
                                move_circles_up(feedback_skel_list)
                                current_guess_circle_list = [None, None, None, None]
                                guess_color_list = [None, None, None, None]
                            else:
                                create_and_display_final_text(lose_response, g_window)
                                guessing_is_done = True
                else:
                    state_circle.setFill(initial_state_circle_fill) #reseting colors so assignment works smoothly
                    state_color =  initial_state_circle_fill
    sys.exit()

main()