"""
Program: CS 115 Lab 3a
Author: Ian Davidson
Description: This program takes 5 integers from a user, finds the sum of them, computes the mean of the imputed numbers
"""


def main():
    total = 0

    for i in range(1, 6):
        usernumber = int(input("Enter an integer: "))
        total += usernumber
    print('The total is:', total)
    total_mean = total/5
    print("The mean is:", total_mean)

main()
