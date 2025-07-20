def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    elif mark >= 50:
        return 'E'
    else:
        return 'F'

def main():
    num_students = int(input("Enter number of students: "))
    students = {}

    for _ in range(num_students):
        name = input("Name: ").strip()
        mark = float(input(f"Marks for {name}: "))
        students[name] = mark

    print("\n--- Student Grades ---")
    report_lines = []
    total = 0
    highest = ('', -1)
    lowest = ('', 101)

    for name, mark in students.items():
        grade = get_grade(mark)
        report_line = f"{name} -> {grade}"
        print(report_line)
        report_lines.append(report_line)
        total += mark

        if mark > highest[1]:
            highest = (name, mark)
        if mark < lowest[1]:
            lowest = (name, mark)

    average = total / num_students
    summary = [
        f"\nClass Average: {average:.2f}",
        f"Topper: {highest[0]} ({highest[1]})",
        f"Lowest: {lowest[0]} ({lowest[1]})"
    ]

    print("\n".join(summary))
    report_lines += summary

if __name__ == "__main__":
    main()
