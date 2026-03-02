# Student Grade System

def calculate_result(name, marks):
    # Calculate average
    average = sum(marks) / len(marks)

    # Determine pass/fail (assuming pass mark is 40 in each subject)
    status = "Pass"
    for mark in marks:
        if mark < 40:
            status = "Fail"
            break

    # Return formatted result
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == "__main__":
    # Taking input
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    # Calculate and print result
    result = calculate_result(name, marks)
    print(result)