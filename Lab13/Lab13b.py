"""
Program: Lab 13b
Author: Ian Davidson
Define and test a basic City class.
"""
import sys


class City:
    def __init__(self, name, pop):
        self.name = name
        self.pop = pop

    def __str__(self):
        return str(self.name) + ' (pop. ' + str(self.pop) + ')'

    def __lt__(self, other):
        if self.pop < other.pop:
            return True
        else:
            return False

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
        if list[i] < min_value:
            min_value = list[i]
            min_idx = i

    return min_idx

def selection_sort(L):
    '''
    Use the selection sort algorithm to sort a list.
    Parameter: unsorted list
    Sorts the original list that was passed to it -- doesn't return anything.
    '''
    for i in range(len(L)-1):
        min_unsorted = find_index_of_min(L, i)
        place = L[i]
        L[i] = L[min_unsorted]
        L[min_unsorted] = place
        #print('Swapped elements', L[i], "and", L[min_unsorted], "--", i, 'and', min_unsorted)


def print_list(list_to_print):
    '''
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    '''

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")


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


def main():
    #tokyo = City('Tokyo', 13189000)
    #mexico_city = City('Mexico City', 8857188)
    # Print whichever city is larger
    #print('The larger city is:')
    #if mexico_city < tokyo:
        #print(tokyo)
    #else:
        #print(mexico_city)
    #testlist= [tokyo, mexico_city]
    filename = input("enter name of file: ")
    testlist = readfile(filename)
    print()
    city_list = []
    for i in range(len(testlist)//2):
        new_city = City(testlist[i*2], int(testlist[i*2+1]))
        city_list.append(new_city)
    print('The original list of cities is:')
    print_list(city_list)
    selection_sort(city_list)
    print()
    print('The new list of cities is: ')
    print_list(city_list)



main()
