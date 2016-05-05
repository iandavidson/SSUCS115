"""
Program: CS 115 Lab 10c
Author: Ian Davidson
Description: This program will open a file and then search its contents
             using linear and binary search.
"""


def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """

    infile = open(filename, "r")  # open file for reading

    # Use Python's file read function to read the file contents
    filetext = infile.read().splitlines()
    #print('Number of lines in file:', len(filetext))
    infile.close()  # close the file

    return filetext  # the text of the file, as a single string

def print_list(list_to_print):
    for i in range(len(list_to_print)):
        print(i , ":" , list_to_print[i])


def linear_search(search_list, value_to_find):
    for i in range(len(search_list)):
        if search_list[i] == value_to_find:
            return i
    return None


def binary_search(search_list, value_to_find):
    """
    Uses a binary search function to find the position of an item in a list
    Parameters: the list; the item to search for
    Returns: the position of the item in the list
             (or None if it is not in the list)
    """
    accume = 1
    start = 0
    end = len(search_list)-1
    while True:
        middle_index = (start + end)//2
        middle_value = search_list[middle_index]
        print(middle_value)
        if middle_value > value_to_find:
            end = middle_index - 1
        elif middle_value < value_to_find:
            start = middle_index + 1
        elif middle_value == value_to_find:
            print("**Binary search iterations: ", accume)
            return middle_index
        accume += 1
        if (start == end) and (value_to_find != search_list[middle_index]):
            print("**Binary search iterations: ", accume)
            return None



def main():
    """ Read and print a file's contents. """

    user_choice = input('Name of input file: ')
    print()
    read_file = readfile(user_choice)
    lin_idx = None
    bin_idx = None
    print("The original list of cities is: ")
    print_list(read_file)
    read_file.sort()
    print()
    print("After sorting, the new list is: ")
    print_list(read_file)
    print()
    go_on = ''
    while True:
        go_on = input('Enter the name of a city: ')
        if go_on == 'quit':
            break
        lin_idx = linear_search(read_file, go_on)
        print('Linear search: ', lin_idx)
        bin_idx = binary_search(read_file, go_on)
        print('Binary search: ', bin_idx)
        print()


main()