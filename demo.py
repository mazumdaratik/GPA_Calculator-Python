def calculate_gpa(marks):
    average = sum(marks) / len(marks)
    return average

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif 81 <= average <= 90:
        return "A"
    elif 71 <= average <= 80:
        return "B"
    elif 61 <= average <= 70:
        return "C"
    elif 41 <= average <= 60:
        return "D"
    else:
        return "F"

def main():
    subjects = ["Bangla", "English", "Math", "Science"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter the marks for {subject}: "))
                if 1 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 1 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    average_marks = calculate_gpa(marks)
    grade = calculate_grade(average_marks)

    print(f"\nAverage Marks: {average_marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()