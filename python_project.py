# Python Grade Book Project

# used for file selection 
from easygui import *

import sys

# List program features and returns users choice
def gradebookOptions():
    selection = 0
    while selection > 6 or selection < 1:
        print("1. Show grades\n")
        print("2. Show student\n")
        print("3. Change grade\n")
        print("4. Add student\n")
        print("5. Delete student\n")
        print("6. Show statistics\n")
        selection = int(input("Please type in the number corresponding to the action you want to perform: "))

        if selection > 6 or selection < 1:
            print("Selection not valid. Select an option 1 through 6.\n")

    return selection

# List all of the students and their grades
def listStudents(gradebook):
    print("Listing students and their grades:\n")

    for i in gradebook:
        print(*i)

    print("Listing completed\n")

# Shows the name and grade of a specific student
def showStudent(gradebook, student):
    name = student.split() # get student's first and last name
    for i in gradebook:
        if i[0] == name[0] and i[1] == name[1]:
            print("{0} {1}'s grade is {2}".format(i[0], i[1], i[2]))
            return
    print("{0} {1} could not be found".format(name[0], name[1]))

# Changes the grade of a student
def changeGrade(gradebook, student, grade):
    name = student.split() # get student's first and last name
    for i in gradebook:
        if i[0] == name[0] and i[1] == name[1]:
            i[2] = grade
            print("{0} {1}'s grade has been changed".format(i[0], i[1]))
            return
        
    print("{0} {1} could not be found".format(name[0], name[1]))

# Adds a student
def addStudent(gradebook, student, grade):
    name = student.split() # get student's first and last name
    gradebook.append([name[0], name[1], grade])

    print("{0} {1} has been added".format(name[0], name[1]))
    
# Deletes a student from the class
def deleteStudent(gradebook, student):
    name = student.split() # get student's first and last name
    for i in gradebook:
        if i[0] == name[0] and i[1] == name[1]:
            gradebook.remove(i)
            print("{0} {1} has been removed".format(name[0], name[1]))
            return

    print("{0} {1} was not found".format(name[0], name[1]))
    
# Shows class statistics
def showStatistics(gradebook):
    # average class grade
    total = 0
    for i in gradebook:
        total += int(i[2])

    average = total / len(gradebook)

    print("The class average is: {0}".format(average))
        
    # min grade
    mingrade = 100
    for i in gradebook:
        if int(i[2]) < mingrade:
            mingrade = int(i[2])
            
    print("The min grade is: {0}".format(mingrade))

    # max grade
    maxgrade = 0
    for i in gradebook:
        if int(i[2]) > maxgrade:
            maxgrade = int(i[2])
            
    print("The max grade is: {0}\n".format(maxgrade))   



# Main Program

answer = "null" #default value

while (answer != "y"):
    answer = input("Press y to select your file or n to close the program: ")
    if answer == "n":
        sys.exit()
        
path = fileopenbox() #Opens up file selection box

grade_file = open(path, 'r')

gradebook = [] # empty list to store the files content in

# goes through each line of grade_file
for aline in grade_file:
    values = aline.split() # split the lines at white space
    gradebook.append([values[0], values[1], values[2]]) # stores a list of each string in a line in the gradebook list

grade_file.close()
# Message to let the user now the file was imported
# PROGRAM DOES NOT CHECK IF FILE WAS IN THE CORRECT FORMAT 
print("Student names and grades have been importorted\n")


answer = gradebookOptions()

while answer != 7:

    if answer == 1: # List
        listStudents(gradebook)
    elif answer == 2: # show student
        student = input("Enter the first and last name of the student you want to view: ")
        showStudent(gradebook, student)
    elif answer == 3: # change grade
        student = input("Enter the first and last name of the student you want to change the grade for: ")
        grade = input("Enter the student's new grade: ")
        changeGrade(gradebook, student, grade)
    elif answer == 4: # add student
        student = input("Enter the first and last name of the student you want to add: ")
        grade = input("Enter the student's grade: ")
        addStudent(gradebook, student, grade)
    elif answer == 5: # delete student
        student = input("Enter the first and last name of the student you want to remove: ")
        deleteStudent(gradebook, student)
    else: # asnwer was 6 / statistics
        showStatistics(gradebook)

    answer = int(input("If you would like to quit the program, type in 7, otherwise, select another action: "))
    

# out of loop, user chose to quit the program
# open file in write mode
grade_file = open(path, 'w')

# write new grades to file
for lst in gradebook:
    line = "{} {} {}\n".format(lst[0], lst[1], lst[2])
    grade_file.write(line)
# close file
grade_file.close()
# close program
sys.exit()

    
    
        
    
    
    
