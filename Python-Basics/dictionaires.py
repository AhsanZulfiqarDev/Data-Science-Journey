D={23: "value",'B':43,'C':'CCD'}
print(D)
print("The type of L is:",type(D))
print(D[23])
print(D['B'])
D['newKey']= "newValue"
print(D)
D2={"y":"YY","z":"ZZ"}
del D[23]
print(D)
##concatenate two dictionaries
##update method is used to concatenate two dictionaries
import os
import sys

sys.path.append(os.path.dirname(__file__))

import lists
import sets
import tuples

D4 = {'A': lists.L, 'B': sets.s, 'C': tuples.T, 'D': D}
print(D4['A'][len(D4['A'])-1])

"""Let say you  are a teacher and you have different 
students records containing id of a student and the marks
list in each subject where different students have taken 
different numbers of subjects.All these records are in a 
hard copy. You want to enter all the data in computer and
want to compute the average marks of each sudent and display"""
def getDataFromUser():
    D = {}
    while True:
        try:
            studentID = input("Enter student ID (press Enter to stop): ").strip()
            if not studentID:
                break

            marksList = input("Enter marks list separated by space: ").strip()
            moreStudents = input('Enter "no" to quit insertion: ').strip().lower()

            if studentID in D:
                print(studentID, "is already present")
            else:
                D[studentID] = marksList.split()

            if moreStudents == "no":
                break
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted. Returning current dictionary.")
            break

    return D


studentData = getDataFromUser()
print(studentData)

def getAvgMarks(D):
    avgMarks = {}
    for student_id, marks in D.items():
        if not marks:
            avgMarks[student_id] = 0
            continue
        total = sum(int(mark) for mark in marks)
        avgMarks[student_id] = total / len(marks)
    return avgMarks


avgM = getAvgMarks(studentData)
for student_id, avg in avgM.items():
    print("The average marks of student with ID:", student_id, "is:", avg)
    
    