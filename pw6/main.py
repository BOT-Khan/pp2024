import pickle
from input import *
from output import *
from domains.student import Student
from domains.course import Course
def main():
    students = []
    courses = []
    marks = {}

    num_students = number_of_students()
    for _ in range(num_students):
        stu_id, stu_name, stu_date = input_student_information()
        students.append(Student(stu_id, stu_name, stu_date))

    num_courses = number_of_courses()
    for _ in range(num_courses):
        cou_id, cou_name = course_information()
        courses.append(Course(cou_id, cou_name))

    while True:
        pass

if __name__ == "__main__":
    main()
