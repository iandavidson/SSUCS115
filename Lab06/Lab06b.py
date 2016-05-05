"""
Program: CS 115 Lab 6b
Author: Ian Davidson
Description: This program will read a positive integer and
 find the largest power of two that is less than or equal to it.
"""


def main():
     # Read user's input and store it in a variable called i_num.
    i_num = int(input("Enter a number:"))
     # Initialize a variable n to serve as the exponent.
    n = 0
    # Initialize a variable two_to_n to hold the value of 2**n
    two_to_n = 2**n
    while two_to_n < i_num:
        n += 1
        two_to_n *= 2
    if two_to_n > i_num:
        n -= 1
        two_to_n /= 2


    print("2**" + str(n))


main()