student_data = [
{
"ID": 1,
"Name": "Alice",
"Age": 20,
"Major": "Computer Science",
"GPA": 3.7
},
{
"ID": 2,
"Name": "Bob",
"Age": 21,
"Major": "Engineering",
"GPA": 3.9
},
{
"ID": 3,
"Name": "Hassan",
"Age": 20,
"Major": "Computer Science",
"GPA": 3.7
},
{
"ID": 4,
"Name": "Mariam",
"Age": 21,
"Major": "Engineering",
"GPA": 3.9
}
]




a = int(input("""
1 = Get Student by ID
2 = Get All Students
3 = Get Students by Major
4 = Add Student
5 = Find Common Majors
6 = Delete Student
7 = Calculate Average GPA
8 = Get Top Performers
9 = Exit
        
choose your option : """))

if a == 1 :

    id = int(input("enter student's ID : "))
    def findStudentByID(student_data, id):
        for student in student_data:
            if id == student["ID"]:
                return student
        else :
            return "not found"
    print(findStudentByID(student_data, id))            


if a == 2 :

    for student in student_data:
        print(f"ID: {student['ID']}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Major: {student['Major']}")
        print(f"GPA: {student['GPA']}")
        print(f"---------------------------")


if a == 3 :

    major = input("enter the major : ")
    students_of_same_major = []
    def findStudentsByMajor(student_data, major):
        for student in student_data:
            if major == student["Major"]:
                students_of_same_major.append(student["Name"])
        return students_of_same_major   
    print(findStudentsByMajor(student_data, major))


if a == 4 :

    
    def addStudent(student_data):
    
        new = {
            "Name" :input("name: "),
            "Age":int(input("age: ")),
            "Major":input("major: "),
            "GPA":float(input("GPA: "))
        }
        
        student_data.append(new)
        return student_data
    
    print(addStudent(student_data))


# Choice 5 This function takes two student data lists as arguments and returns a set of common
# majors found in both lists.


if a == 6 :


    def removeStudent(student_data):
        r = int(input("enter student's ID: "))
        
        for student in student_data:
            if student["ID"] == r:
                student_data.remove(student)
        return student_data

    print(removeStudent(student_data))

if a == 7:

    def averageGPA(student_data):
        allGPA=0
        
        for student in student_data:
            allGPA += student["GPA"]

        averageGPA = allGPA / len(student_data)
        return averageGPA

    print(averageGPA(student_data))

# Choice 8: This function takes the student data and the number of top-performing students to
# retrieve as arguments. It returns a tuple of the specified number of students with the highest
# GPAs (the tuple should have the name of those students).
# Choice 9: This choice terminates the program.