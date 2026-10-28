# Student Performance Analysis System

def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def highest_marks(marks):
    return max(marks)

def lowest_marks(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = int(input("Enter mark of subject: "))
        marks.append(mark)

    total = total_marks(marks)
    average = average_marks(marks)
    highest = highest_marks(marks)
    lowest = lowest_marks(marks)
    g = grade(average)

    students.append((name, total, average, highest, lowest, g))

# Sort students by total marks using lambda
students.sort(key=lambda x: x[1], reverse=True)

print("\n--- Student Performance ---")

for student in students:
    print("\nName:", student[0])
    print("Total:", student[1])
    print("Average:", round(student[2], 2))
    print("Highest:", student[3])
    print("Lowest:", student[4])
    print("Grade:", student[5])