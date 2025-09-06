# 12. Student class
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Class:", self.student_class)
