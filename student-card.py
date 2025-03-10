# Student Report Card

def get_student_data():
    name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")

    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    return name, roll_number, marks

def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

def display_report_card(name, roll_number, marks, total_marks, percentage, grade):
    print("\n------------------------------------")
    print(f" Report Card - {name} (Roll No: {roll_number})")
    print("------------------------------------")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    print("------------------------------------")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("------------------------------------\n")

def main():
    print("Welcome to Student Report Card Generator")
    
    students = []
    while True:
        name, roll_number, marks = get_student_data()
        total_marks = sum(marks.values())
        percentage = total_marks / len(marks)
        grade = calculate_grade(percentage)

        students.append((name, roll_number, marks, total_marks, percentage, grade))

        print(f"Record of {name} inserted successfully.")
        if input("Do you want to insert more? (Y/N): ").strip().upper() != 'Y':
            break

    print("\nFinal Report Cards:")
    for student in students:
        display_report_card(*student)

if __name__ == "__main__":  
    main()
