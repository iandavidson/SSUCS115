"""
Program: CS 115 Lab 10b
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


def main():
    """ Read and print a file's contents. """

    user_choice = input('Name of input file: ')

    read_file = readfile(user_choice)
    idx = None
    print_list(read_file)
    go_on = ''
    while go_on != 'quit':
        idx = None
        go_on = input('Enter the name of a city: ')
        idx = linear_search(read_file, go_on)
        if idx != None:
            print('The Position of', go_on, 'is:')
            print('Linear search: ', idx)
            print()
main()