def calculate_statistics(grades):
    if not grades:
        return {
            'average': None,
            'highest': None,
            'lowest': None,
            'count': 0
        }

    total = sum(grades)
    average = total / len(grades)
    highest = max(grades)
    lowest = min(grades)
    count = len(grades)

    return {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'count': count
    }

def get_grades_from_input():
    grades = []
    while True:
        try:
            grade_input = input("Enter a grade (or 'done' to finish): ")
            if grade_input.lower() == 'done':
                break
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Invalid grade. Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    return grades

def display_statistics(statistics):
    if statistics['count'] == 0:
        print("No grades entered.")
        return

    print("\n--- Grade Statistics ---")
    print(f"Number of Grades: {statistics['count']}")
    print(f"Average Grade: {statistics['average']:.2f}")
    print(f"Highest Grade: {statistics['highest']:.2f}")
    print(f"Lowest Grade: {statistics['lowest']:.2f}")

def main():
    print("Welcome to the Grade Statistics Calculator!")
    grades = get_grades_from_input()
    statistics = calculate_statistics(grades)
    display_statistics(statistics)
    print("Thank you for using the Grade Statistics Calculator!")

if __name__ == "__main__":
    main()