"""
Program: CS 115 Lab 11a
Author: Ian Davidson
Description: this programs uses a file to to find the lowest value. Can start at any index in list
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

def find_index_of_min(list, start):
    '''
    Finds the minimum value in the list and returns it's index, list can also start at an index and look beyond it
    while looking for min.
    '''
    if len(list) < start:
        return None
    min_value = list[start]
    min_idx = start
    for i in range(start, len(list)):
        if min_value > list[i]:
            min_value = list[i]
            min_idx = i

    return min_idx


def main():
    """ Read and print a file's contents. """

    user_choice = input('Name of input file: ')
    print()
    read_file = readfile(user_choice)

    print("The original list of cities is: ")
    print_list(read_file)


main()