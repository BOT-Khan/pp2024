#cou = course
#stu = student

def number_of_students():
    return int(input("Number of Students is: "))

def input_student_information():
    stu_id = input("Student ID: ")
    stu_name = input("Student Name: ")
    stu_date = input("Date of Birth (Format: DD/MM/YYYY): ")
    return {'id': stu_id, 'name': stu_name, 'date': stu_date}

def number_of_courses():
    return int(input("Number of courses is: "))

def course_information():
    cou_id = input("Course ID: ")
    cou_name = input("Course Name: ")
    return {'id': cou_id, 'name': cou_name}

def input_marks(students):
    cou_id = input("Enter course ID: ")
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} (ID {student['id']}): "))
        marks[student['id']] = mark
    return cou_id, marks

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Date: {student['date']}")

def show_student_marks(cou_id, marks, students):
    print(f"Marks for Course {cou_id}:")
    for student in students:
        stu_id = student['id']
        if stu_id in marks:
            print(f"Student {student['name']} ({stu_id}): {marks[stu_id]}")
        else:
            print(f"Student {student['name']} ({stu_id}): Not available")

def main():
    students = []
    courses = []
    marks = {}

    num_students = number_of_students()
    for _ in range(num_students):
        students.append(input_student_information())

    num_courses = number_of_courses()
    for _ in range(num_courses):
        courses.append(course_information())

    while True:
        print(" ")
        print("Options:")
        print("1. Input Marks")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Course")
        print("5. Exit")
        choice = input("Choose Option: ")

        if choice == '1':
            cou_id, mark = input_marks(students)
            marks[cou_id] = mark
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            cou_id = input("Enter Course ID: ")
            if cou_id in marks:
                show_student_marks(cou_id, marks[cou_id], students)
            else:
                print("Error. This student doesn't have a mark. \nPlease add a mark.")
        elif choice == '5':
            print("Goodbye.")
            break
        else:
            print("No valid choice. Try again.")

if __name__ == "__main__":
    main()
