'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
'''



# get second lowest marks
'''
solution pseudo-code: 
find second highest score -> find matching score -> sort their name by alphabet
'''
def secondLowestStudents(studentsList_input,indivisual_score):
    second_lowest = sorted(list(set(indivisual_score)))[1]
    matchingStudents = []
    for i in range(len(studentsList_input)):
        if studentsList_input[i][1] == second_lowest:
            matchingStudents.append(studentsList_input[i][0])
    matchingStudents = list(set(matchingStudents))
    matchingStudents = sorted(matchingStudents)
    
    for student_name in matchingStudents:
        print(student_name)


if __name__ == '__main__':
    studentsList = []
    eachStudent = []
    eachStudentscore = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        eachStudentscore.append(score)
        eachStudent=[name,score]
        studentsList.append(eachStudent)
    # function call
    secondLowestStudents(studentsList,eachStudentscore)
