"""
Program: CS 115 Lab 9a
Author: Ian Davidson
Description: This program will create a magic square
   whose size is specified by the user.
"""
import sys

def create_list(rows, cols):
    """
    Creates a two-dimensional array.

    Parameters: the numbers of rows and columns

    Returns: a 2D array with all values set to zero
    """

    two_d = []  # create an empty list
    for i in range(rows):
        two_d.append([])  # append an empty list to two_d
        for j in range(cols):
            two_d[i].append(0)   # two_d[i] is the empty list that we just created.
                                 # here, we are adding elements to it.
    return two_d


def rjust_by_n(number, n):
    """
    Return a string of length "n" with number right-justified in it.

    Parameters:
    number: an value with n or fewer digits
    n: a positive integer value

    Returns: a string of length n with a number right-justified in it.
    """
    return str(number).rjust(n)


def print_list(numbers):
    """
    Print a 1D list of numbers, where each number is right-justified
    """
    for i in range(len(numbers)):
        print( rjust_by_n(numbers[i], 4), end ='')
    print()

def build_magic_square(square):
    """
    Create a magic square in "square"

    Parameter:
    square: a two dimensional array whose number of rows and columns are equal
            and len(square) is an odd number.

    Modifies "square" but doesn't return anything.
    """
    magic_value = 1
    square_size = len(square)
    row = 0
    col = square_size // 2
    square_size_squared = square_size * square_size
    while magic_value <= square_size_squared:
        square[row][col] = magic_value
        row -= 1
        col += 1
        if row < 0 and col > square_size - 1:
            row += 2
            col -= 1
        elif row < 0:
            row = square_size - 1
        elif col > square_size - 1:
            col = 0
        elif square[row][col] != 0:
            row += 2
            col -= 1

        magic_value += 1


def print_2d_list(two_d_list):
    """
    Print a 2-dimensional list
    """
    for i in range(len(two_d_list)):
        print_list(two_d_list[i])


def main():
    square_size = int(input("Enter an odd integer to build a magic square: "))
    if square_size % 2 != 1:
        print(square_size , "is not an odd integer. Terminating...")
        sys.exit()
    square = create_list(square_size, square_size)
    build_magic_square(square)
    print_2d_list(square)




main()