# 8. Function attributes
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

print(student.__code__.co_varnames)  # function attributes
