"""
Program: CS 115 Lab 6c
Author: Ian Davidson
Description: This program will read a positive integer and
 express it as the sum of powers of 2.
"""


def main():
    i_num = int(input("Enter a number:"))
    # Read user's input and store it in a variable called i_num.25
    # Outer loop:
    while i_num > 0 :       # while i_num is larger than zero:
        n = 0
        two_to_n = 2**n
        while two_to_n < i_num:
            n += 1
            two_to_n *= 2
        if two_to_n > i_num:
            n -= 1
            two_to_n /= 2
        # Initialize n and two_to_n.
        i_num = i_num - two_to_n
        # Do all the stuff you were doing before to find n and two_to_n.
        # Remember that two_to_n is the largest power of 2 less than i_num.
        print("2**" + str(n), end="")
        if i_num != 0:
            print(" + ", end="")

    print()

main()