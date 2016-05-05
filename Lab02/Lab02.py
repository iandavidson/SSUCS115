"""
Program: CS 115 Lab 2
Author: Ian Davidson
Description: This program will compute the volume of a cube and sphere, area of a square, triangle, and circle
    given the side length/radius.
"""

import math

def main():
    # Get the side length
    length = float(input('Enter a numeric value: '))

    # Compute the area of the square
    square_area = length * length
    circle_area = math.pi * length**2
    cube_volume = length**3
    sphere_volume = 4/3*math.pi*length**3
    triangle_area = length**2*math.sqrt(3)/4

    print("The area of a square with side length ", length,
          " is ", square_area, ".", sep="")
    print("The area of a circle with radius length ", length,
          " is ", circle_area, ".", sep="")
    print("The volume of a cube with edge length ", length,
          " is ", cube_volume, ".", sep="")
    print("The volume of a sphere with radius length ", length,
          " is ", sphere_volume, ".", sep="")
    print("The area of an equilaeral riangle with side length ", length,
          " is ", triangle_area, ".", sep="")
main()