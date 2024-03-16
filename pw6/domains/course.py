class Course:
    def __init__(cou, cou_id, cou_name):
        cou.id = cou_id
        cou.name = cou_name

    def __str__(cou):
        return f"Course ID: {cou.id}, Name: {cou.name}"
