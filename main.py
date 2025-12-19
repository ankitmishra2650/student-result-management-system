# Student Result Management System

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    print("----- Student Result Management System -----")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []
    subjects = ["Maths", "Science", "English", "Computer", "Social"]

    for subject in subjects:
        score = float(input(f"Enter marks for {subject}: "))
        marks.append(score)

    total = sum(marks)
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    print("\n----- Result -----")
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    # Save result to file
    with open("results.txt", "a") as file:
        file.write(f"{name}, {roll_no}, {total}, {percentage}, {grade}\n")

    print("\nResult saved successfully!")

if __name__ == "__main__":
    main()
