"""
Program: CS 115 Lab 7b
Author: Ian Davidson
Description: Computes the average word length of the user's text based off of character length of words.
"""


def main():

    total_word = 0
    total_char = 0
    s = input("Enter some text: ")
    while s != "":
        words = s.split()
        total_word += len(words)
        for i in words:
            total_char += len(i)
        s = input("Enter some text: ")
    try:
        avg_word = total_char/total_word
        print("The average word length is:", avg_word)
    except Exception as e:
        print("You did not enter any words.")




main()
