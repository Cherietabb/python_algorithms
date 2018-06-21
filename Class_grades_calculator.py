def letter_grade(grade):
    if grade >= 90:
        print("A")
        print("You're a rock star!")
    elif grade >= 80:
        print("B")
        print("Way to go!")
    elif grade >= 70:
        print("C")
        print("Whew! You made it!")
    elif grade >= 60:
        print("D")
        print("Well, there's always Liberal Arts.")
    else:
        print("Programming is made more difficult if it isn't practiced daily.")


def get_class_average(total, grade, num_of_students):
    get_class_average = total / num_of_students
    return get_class_average


def main():
    print("Class grades calculator. \nPlease follow prompts to calculate grade.")
    num_of_students = int(input("Enter the number of students: "))
    total = 0.0
    for i in range(0, num_of_students):
        grade = int(input('grade: '))
        letter_grade(grade)
        total += grade
    print("Class average is: ", get_class_average(total, grade, num_of_students))

if __name__ == "__main__":
    main()



