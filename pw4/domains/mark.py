from course import Course

class Mark:
    def __init__(score, cou_id, cou_marks):
        score.id = cou_id
        score.marks = cou_marks

    def __str__(score):
        return f"Marks for Course {score.id}: {score.marks}"
