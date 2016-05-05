"""
Program: CS 115 Lab 11b
Author: Ian Davidson
Description: This program will open a file and then sort using Selection sort from least to greatest.
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

def selection_sort(L):
    '''
    Use the selection sort algorithm to sort a list.
    Parameter: unsorted list
    Sorts the original list that was passed to it -- doesn't return anything.
    '''
    swap_count = 0
    for i in range(len(L)-1):
        min_unsorted = find_index_of_min(L, i)
        #if min_unsorted != i:
        place = L[i]
        L[i] = L[min_unsorted]
        L[min_unsorted] = place
        print('Swapped elements', i, "and", min_unsorted, "--", L[i], 'and', L[min_unsorted])

def main():
    """ Read and print a file's contents. """

    user_choice = input('Name of input file: ')
    print()
    read_file = readfile(user_choice)

    print("The original list of cities is: ")
    print_list(read_file)
    print()
    print("The new list of cities is: ")
    selection_sort(read_file)
    print_list(read_file)

main()