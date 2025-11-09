# Program: Display grade based on student marks
def student_grade(marks):
    match marks:
        case marks if marks >= 90:
            return "Grade: A+ (Excellent)"
        case marks if marks >= 80:
            return "Grade: A (Very Good)"
        case marks if marks >= 70:
            return "Grade: B (Good)"
        case marks if marks >= 60:
            return "Grade: C (Average)"
        case marks if marks >= 50:
            return "Grade: D (Pass)"
        case marks if marks < 50:
            return "Grade: F (Fail)"
        case _:
            return "Invalid marks"

# Example usage
mark = int(input("Enter student marks (0–100): "))
print(student_grade(mark))
