students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 92)]

total_grades = 0
student_count = len(students)

for student in students:
    name, grade = student
    print(f"Student: {name}, Grade: {grade}")
    total_grades+= grade
average_grade = total_grades / student_count
print(f"The average grade is", average_grade)