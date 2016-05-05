"""
Program: CS 115 Lab 7a
Author: Ian Davidson
Description: This program finds $1.00 words.
"""


def main():
    total = 0
    # Ask the user for a word, and save the word to a variable.
    word = input("Enter a word: ")
    # Convert the user's word to lowercase
    word = word.lower()
    # As long as the user's word is not 'quit'...
    while word != 'quit':
        for i in word:
            num = int(ord(i)) - 96
            total += num
        total/= 100
        total = "{0:.2f}".format(total)
        print("Your word is worth $" + str(total) + ".")
        if (total == "1.00"):
            print("Congratulations!")
        total = 0
        word = input("Enter a word: ")
        word = word.lower()
main()