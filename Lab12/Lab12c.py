"""
Program: Lab 12
Author: Ian Davidson
This program will eventually read in a list of students and grades from a text
 file, calculate the students' averages, and print the list of students.
"""

class Student:
    """ A class that holds the data for an individual student """
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def get_average(self):
        """ Return the average grade """
        accume = 0
        for score in self.scores:
            accume += score
        avg = accume/len(self.scores)
        avg = round(avg, 5)
        return avg


    def print(self):
        """ Print the student info in the following format:
           Name (12 characters), grades(separated by tabs), average (formatted
           to 5 decimals """

        # Right now, just prints the student name padded out to 12 characters
        string_to_print = self.name.ljust(12)
        for score in self.scores:
            string_to_print += '\t' + str(score)

        string_to_print += '\t' + str(self.get_average())

        print(string_to_print)



def read_input_file(filename):
    infile = open(filename, 'r')#opens file for reading
    filetext = infile.read().splitlines()
    infile.close()
    return filetext


# A tester program
def main():
    studentlines = read_input_file("students.txt")
     #Loop over the list of lines from the file and
# break each line down into a name and scores
    avg_accume = 0
    line_list = []
    for i in range(len(studentlines)):
    # 1. Split line into a list. If list is empty, break out of the loop.
        line_list.append(studentlines[i].split())
        if line_list[i] == []:
            break
    # 2. The first item in the list is the student's name
        name = line_list[i][0]
    # 3. Convert the remaining items in the list into integers
        scores = []
        for j in range(1, len(line_list[i])):
            scores.append(int(line_list[i][j]))
    # 4. Create a new Student variable with that name and scores
        new_stud = Student(name, scores)
    # 5. Call the Student print method to print that student's
        new_stud.print()
        avg_accume += new_stud.get_average()
    # information
    print()
    print('Overall average: ', round(avg_accume/len(studentlines), 5))

main()
