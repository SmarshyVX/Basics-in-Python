student_data = {}

def studentadmissions():
    print("Hello there. Welcome to the Student Admission Portal.")
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    grade = float(input("Enter your grade (0-100): "))

    if grade >= 50:
        print(f"Congratulations {name}, you have been admitted to our school")

        student_data["name"] = name
        student_data["age"] = age
        student_data["email"] = email
        student_data["grade"] = grade

        print("This is your student information:", student_data)
        print("Thank you for applying.")

    else:
        print(f"Sorry {name}, you are not eligible for admission.")

studentadmissions()