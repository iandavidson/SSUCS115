"""
Program: CS 115 Lab 8c
Author: Ian Davidson
Description: This program computes geometric quantities, including finding area, volumes of squares, area, volume of
circles and spheres, and gives area of an equilateral triangle.
"""
import sys
import math


def get_numeric_val():
    """
    Ask the user for a number
    Exit if the user does not supply a positive value.
    Otherwise, return the value they entered
    """

    num = float(input('Enter a positive numeric value: '))
    if num <= 0:
        sys.exit('Error: that number was not positive.')
    return num


def get_menu_choice():
    """ Print the menu and return the user's selection """
    print("Would you like to")
    print("a. Calculate the area of a square?")
    print("b. Calculate the area of a circle?")
    print("c. Calculate the volume of a cube?")
    print("d. Calculate the volume of a sphere?")
    print("e. Calculate the area of an equilaeral triangle?")
    print("q. Quit?")
    user_menu = input("")
    new_choice = user_menu.lower()
    return new_choice
def compute_square_area(side):
    """
    Compute and return the area of a square.
    Parameter: side length of the square
    """
    area = side**2
    return area


def compute_circle_area(radius):
    """
    Compute and return the area of a circle.
    Parameter: radius of the circle
    """
    circle_area = radius**2 * math.pi
    return circle_area

def compute_cube_volume(edge):
    """
    Compute and return the volume of a cube.
    Parameter: edge length of the cube
    """
    cube_volume = edge**3
    return cube_volume

def compute_sphere_volume(radius):

    sphere_volume = radius**3 * math.pi * 4/3
    return sphere_volume

def compute_tri_area(side):

    Equil_area = math.sqrt(3)/4 * side**2
    return Equil_area

def main():
    menu_choice = get_menu_choice()  # Get the user's first choice
    while menu_choice != 'q':
        user_num = get_numeric_val()  # Get the side length (etc.)

        if menu_choice == 'a':
            print('The area of a square with side length ',
                  user_num, ' is ', round(compute_square_area(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'b':
            print('The area of a circle with radius length ',
                  user_num, ' is ', round(compute_circle_area(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'c':
            print('The volume of a cube with edge length ',
                  user_num, ' is ', round(compute_cube_volume(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'd':
            print('The volume of a sphere with radius length ',
                  user_num, ' is ', round(compute_sphere_volume(user_num), 5),
                  '.', sep="")
        elif menu_choice == 'e':
            print('The area of a equilateral triangle with side length ',
                  user_num, ' is ', round(compute_tri_area(user_num), 5),
                  '.', sep="")


        menu_choice = get_menu_choice()  # Get user's next choice


main()