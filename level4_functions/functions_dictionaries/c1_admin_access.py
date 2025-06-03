import sys

def add_grade(grades_dict, student, student_grade):
    grades_dict[student] = student_grade
    print(f"Added {student} with grade {student_grade} to the grade dictionary.")

students_grades = {"Alice": 85, "Bob": 90} #initialise student's grades dictionary
add_grade(students_grades, "Alex", 100) #use the add_grade() function to a a grade to the students

admin_password = "%00313&s2%H0!41@@!#%"

def get_grade():
    user_input = input("Enter a student's name then grade, separated by a comma: ")

    name, grade = user_input.split(",")

    name = name.strip()
    grade = grade.strip()

    add_grade(students_grades, name, grade)

def main():

    input_password = input("What is the admin password? (press q to quit): ")
    if input_password.lower() == "q":
        sys.exit()
    elif input_password == admin_password:
        while True:
            print()
            get_grade()
            print(f"Updated grades dictionary: {students_grades}")
            admin_input = input("Would you like to keep adding student's grades? (y/n): ")
            if admin_input.lower() == "n":
                break
            elif not admin_input.lower() == "y":
                print("Invalid input. Shutting down")
                break
    else:
        print("Incorrect password. Shutting down.")

main()