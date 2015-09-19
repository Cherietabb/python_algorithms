# Student grades records.
def main():
    # Open file.
    grades = open('grades.txt', 'w')
    grades.write('Austin Community College Student Records\n')
    grades.write('----------------------------------------\n')
    for count in range(1, 13):
        try:
            print('Austin Community College Student Records')
            # Take input from the user.
            name = input('Enter a name: ')
            grade = int(input('Please enter a grade: '))
            # Check to ensure user inputs letters only.
            if not name.isalnum():
                print('Error: Please enter a valid name.')
            elif grade < 0 or grade > 100:
                print('Error: The grade cannot be less than zero or greater than 100.')
            else:
                print(name, '\t', grade)
                # Write to the file.
                grades.write(name + '\t' + str(grade) + '\n')
        except ValueError:
            print('Invalid input! Please enter a valid numbers only!')
    # Close file.
    grades.close()

    print('Grades added to grades.txt.')

    # Open the grades file for input.
    grades = open('grades.txt', 'r')

    # Read all lines from the file.
    for line in grades:
        # Convert line to an int.
        grade = grades.readline()
        name = grades.readline()
        # Display the grades.
        print(name, '\t', grade)

    # Close the file.
    grades.close()


main()
