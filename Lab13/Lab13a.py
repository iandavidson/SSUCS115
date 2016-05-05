"""
Program: Lab 13a
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


def main():
    tokyo = City('Tokyo', 13189000)
    mexico_city = City('Mexico City', 8857188)
    # Print whichever city is larger
    print('The larger city is:')
    if mexico_city < tokyo:
        print(tokyo)
    else:
        print(mexico_city)

main()
