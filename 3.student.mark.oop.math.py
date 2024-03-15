import math
import numpy as np
import curses

class Student:
    def __init__(stu, stu_id, stu_name, stu_date):
        stu.id = stu_id
        stu.name = stu_name
        stu.date = stu_date

    def __str__(stu):
        return f"ID: {stu.id}, Name: {stu.name}, Date: {stu.date}"

class Course:
    def __init__(cou, cou_id, cou_name):
        cou.id = cou_id
        cou.name = cou_name

    def __str__(cou):
        return f"Course ID: {cou.id}, Name: {cou.name}"

class Mark:
    def __init__(score, cou_id, cou_marks):
        score.id = cou_id
        score.marks = cou_marks

    def __str__(score):
        return f"Marks for Course {score.id}: {score.marks}"

def number_of_students():
    return int(input("Number of Students is: "))

def input_student_information():
    stu_id = input("Student ID: ")
    stu_name = input("Student Name: ")
    stu_date = input("Date of Birth (Format: DD/MM/YYYY): ")
    return Student(stu_id, stu_name, stu_date)

def number_of_courses():
    return int(input("Number of Courses is: "))

def course_information():
    cou_id = input("Course ID: ")
    cou_name = input("Course Name: ")
    return Course(cou_id, cou_name)

def input_marks(students):
    cou_id = input("Enter course ID: ")
    marks = {}
    for student in students:
        mark = float(input("Enter mark for {} ({}): ".format(student.name, student.id)))
        marks[student.id] = math.floor(mark * 10) / 10
    return cou_id, Mark(cou_id, marks)

def calculate_gpa(marks, credits):
    total_marks = np.sum(np.array(list(marks.values())))
    total_credits = np.sum(np.array(list(credits.values())))
    return total_marks / total_credits

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(course)

def list_students(students):
    print("List of Students:")
    for student in students:
        print(student)

def show_student_marks(cou_id, marks, students):
    print("Marks for Course {}:".format(cou_id))
    for student in students:
        stu_id = student.id
        if stu_id in marks.marks:
            print("Student {} ({}): {}".format(student.name, stu_id, marks.marks[stu_id]))
        else:
            print("Student {} ({}): Not available".format(student.name, stu_id))

def main():
    students = []
    courses = []
    marks = {}
    credits = {}

    num_students = number_of_students()
    for _ in range(num_students):
        students.append(input_student_information())

    num_courses = number_of_courses()
    for _ in range(num_courses):
        courses.append(course_information())

    for course in courses:
        credits[course.id] = float(input(f"Enter Credits for {course.name}: "))

    while True:
        print(" ")
        print("Options:")
        print("1. Input Marks")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Course")
        print("5. GPA of Students")
        print("6. Sort Students by GPA")
        print("7. Exit")
        choice = input("Choose Option: ")

        if choice == '1':
            cou_id, mark = input_marks(students)
            marks[cou_id] = mark
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            cou_id = input("Enter course ID: ")
            if cou_id in marks:
                show_student_marks(cou_id, marks[cou_id], students)
            else:
                print("Error. This student doesn't have a mark. \nPlease add a mark.")
        elif choice == '5':
            stu_id = input("Enter student ID: ")
            if stu_id in marks:
                gpa = calculate_gpa(marks[stu_id].marks, credits)
                print(f"GPA of {stu_id} is: {gpa:.2f}")
            else:
                print("No marks to calculate GPA. \nPlease add a mark.")
        elif choice == '6':
            students.sort(key=lambda x: calculate_gpa(marks.get(x.id, {}).marks, credits), reverse=True)
            print("Students sorted by GPA:")
            for student in students:
                print(student)
        elif choice == '7':
            print("Goodbye.")
            break
        else:
            print("No valid choice. Try again.")

if __name__ == "__main__":
    main()
