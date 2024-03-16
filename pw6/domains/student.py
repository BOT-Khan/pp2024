class Student:
    def __init__(stu, stu_id, stu_name, stu_date):
        stu.id = stu_id
        stu.name = stu_name
        stu.date = stu_date

    def __str__(stu):
        return f"ID: {stu.id}, Name: {stu.name}, Date: {stu.date}"