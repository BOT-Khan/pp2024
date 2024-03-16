def number_of_students():
    return int(input("Number of Students is: "))

def input_student_information():
    stu_id = input("Student ID: ")
    stu_name = input("Student Name: ")
    stu_date = input("Date of Birth (Format: DD/MM/YYYY): ")
    return stu_id, stu_name, stu_date

def number_of_courses():
    return int(input("Number of Courses is: "))

def course_information():
    cou_id = input("Course ID: ")
    cou_name = input("Course Name: ")
    return cou_id, cou_name

def input_marks(students):
    cou_id = input("Enter course ID: ")
    marks = {}
    for student in students:
        mark = float(input("Enter mark for {} ({}): ".format(student.name, student.id)))
        marks[student.id] = mark
    return cou_id, marks
