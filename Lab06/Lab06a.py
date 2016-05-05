'''
Program: CS 115 Lab 6a
Author: Ian Davidson
Description: This program will ask the user for a value
   and tell the user whether the value is even or odd.
'''


def main():

    N = int(input('Enter a number: '))

    while (N != 1):
        if N % 2 == 1:
            # Compute the next term in the Collatz sequence for odd N, and set N to that value.
            N = 3*N + 1
            print("The next term is " + str(N) + ".")
        else:
            # Compute the next term in the Collatz sequence for even N, and set N to that value.
            N = N//2
            print("The next term is " + str(N) + ".")

    # Print the new value of N.


main()