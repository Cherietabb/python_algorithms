# This program counts the number of times the letter T
# (uppercase or lowercase) appears in a string.


def count_string():
    # Creat a variable to hold the number.
    count = 0

    # Get a string from the user.
    my_string = input('Enter a sentence: ')

    # Count the Ts.
    for ch in my_string:
        if ch == 't' or ch == 'T':
            count += 1
    print('The letter T appears', count, 'times.')


# Call the main function.
def main():
    count_string()


if __name__ == "__main__":
    main()
