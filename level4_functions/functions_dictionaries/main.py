def add_grade(grades_dict, student, student_grade):
    grades_dict[student] = student_grade
    print(f"Added {student} with grade {student_grade} to the grade dictionary.")

students_grades = {"Alice": 85, "Bob": 90} #initialise student's grades dictionary
add_grade(students_grades, "Alex", 100) #use the add_grade() function to a a grade to the students
print(students_grades)