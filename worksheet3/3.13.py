# 13. Two instances
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

student1 = Student(1, "Alice", "CS")
student2 = Student(2, "Bob", "ME")

print("Student 1:", vars(student1))
print("Student 2:", vars(student2))
