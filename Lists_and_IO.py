# This program will read in the names of students,
# create a list, and write the list to a file.
NUM_STUDENTS = 3


# Add student names to a list.
def get_names(students):
    for index in range(NUM_STUDENTS):
        # Get input from user.
        name = input('Enter student name: ')
        students[index] = name
        index += 1


def main():

    studentlist = open('names.txt', 'w')
    studentlist.write('Student names\n')
    studentlist.write('----------------\n')

    # Create the students list.
    students = [0] * NUM_STUDENTS

    # Create an index variable.
    index = 0
    get_names(students)

    # Display values entered.
    print('Here are the names you entered: ')
    for name in students:
        
        print(name)

    # Print the list sorted alphabetically.
    students.reverse()
    print('Here is the list in reverse: ', students)
    # Print the list in reverse order.
    students.sort()
    print('Here is the list sorted: ', students)
    # Add teacher name to the list.
    students.append('Polanco')
    print('List with teacher name added: ', students)

    # Add my name to index 0.
    students[0] = 'Cherie'
    print('List with my name added: ', students)

    # Convert list to tuple.
    students = tuple(students)
    print(students)
    # Write to the file.
    studentlist.write(str(students) + '\n')

    # Close the file.
    studentlist.close()
    print('New items saved to file')

    
# Call the main function.
main()
