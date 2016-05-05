"""
Program: CS 115 Lab 11c
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
        place = L[i]
        L[i] = L[min_unsorted]
        L[min_unsorted] = place
        print('Swapped elements', i, "and", min_unsorted, "--", L[i], 'and', L[min_unsorted])


def merge(L, start_index, sublist_size):
    """
    Merge two sublists of a list L

    Parameters:
    L - the list
    start_index - the index of the first element to be merged
    sublist_size - the size of the chunks to be merged

    Left chunk: L[start_index] to L[start_index + sublist_size - 1]
    Right chunk: L[start_index + sublist_size] to L[start_index + 2 * sublist_size - 1]
    """

    index_left = start_index
    left_stop_index = start_index + sublist_size
    index_right = start_index + sublist_size
    right_stop_index = min(start_index + 2 * sublist_size,
                           len(L))

    print('Merging sublists:', L[index_left:left_stop_index], 'and',
          L[index_right:right_stop_index]);

    L_tmp = []

    while (index_left < left_stop_index and
           index_right < right_stop_index):
        if L[index_left] < L[index_right]:
           L_tmp.append(L[index_left])
           index_left += 1
        else:
           L_tmp.append(L[index_right])
           index_right += 1

    if index_left < left_stop_index:
           L_tmp.extend(L[index_left : left_stop_index])
    if index_right < right_stop_index:
           L_tmp.extend(L[index_right : right_stop_index])

    L[start_index : right_stop_index] = L_tmp
    print('Merged sublist:', L_tmp, '\n')


def merge_sort(L):
    """
    Sort a list L using the merge sort algorithm.

    (Starter code doesn't fully sort the list.)
    """
    chunksize = 1  # Start by dividing the list into N sub-lists of 1 element each
    while chunksize < len(L):
        print("\n*** Sorting sublists of size", chunksize)

        # Divide the list into pairs of chunks
        left_start_index = 0  # Start of left chunk in each pair

        # While we still have chunks to merge
        while left_start_index + chunksize < len(L):
            merge(L, left_start_index, chunksize)

            # Move to next pair of chunks
            left_start_index += 2 * chunksize

        print('List is now', L)
        chunksize = chunksize * 2


def main():
    """ Read and print a file's contents. """

    user_choice = input('Name of input file: ')
    read_file = readfile(user_choice)
    user = input("Type S for selection sort and M for merge sort: ")
    print("The original list of cities is: ")
    print_list(read_file)
    print()
    user = user.lower()
    if user == 's':
        print("The new list of cities is: ")
        selection_sort(read_file)
        print_list(read_file)
    if user == 'm':
        print("The new list of cities is: ")
        merge_sort(read_file)
        print_list(read_file)





main()