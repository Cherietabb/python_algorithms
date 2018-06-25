import my_conversions

# Constants for menu options.
MILES_TO_KILOMETERS_CHOICE = 1
FAHRENHEIT_TO_CELSIUS_CHOICE = 2
GALLONS_TO_LITERS_CHOICE = 3
POUNDS_TO_KILOGRAMS_CHOICE = 4
INCHES_TO_CENTIMETERS_CHOICE = 5
QUIT_CHOICE = 6

ROWS = 12
COLS = 2


def get_values():
    # Create a two-dimensional list.
    values = [[0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0],
              [0, 0]]
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        # Get user's choice.
        choice = int(input('Enter a number from the menu (from 1 to 6): '))
        if choice == MILES_TO_KILOMETERS_CHOICE:
            # Fill the table with values.
            miles = 0
            for r in range(ROWS):
                values[r][0] = miles
                values[r][1] = my_conversions.convert_kilometers(miles)
            # Print the list.
            print('Miles', '\tKilometers')
            print('-----------------------')
            for r in range(ROWS):
                print(miles, '     \t', format(my_conversions.convert_kilometers(miles), '.2f'))
                miles += 10

        elif choice == FAHRENHEIT_TO_CELSIUS_CHOICE:
            # Fill the table with values.
            fahrenheit = - 10
            for r in range(ROWS):
                values[r][0] = fahrenheit
                values[r][1] = my_conversions.convert_celsius(fahrenheit)
            # Print the list.
            print('Fahrenheit', '\tCelsius')
            print('-----------------------')
            for r in range(ROWS):
                print(fahrenheit, '     \t', format(my_conversions.convert_celsius(fahrenheit), '.2f'))
                fahrenheit += 10
        elif choice == GALLONS_TO_LITERS_CHOICE:
            # Fill the table with values.
            gallons = 0
            for r in range(ROWS):
                values[r][0] = gallons
                values[r][1] = my_conversions.convert_liters(gallons)
            # Print the list.
            print('Gallons', '\tLiters')
            print('-----------------------')
            for r in range(ROWS):
                print(gallons, '     \t', format(my_conversions.convert_liters(gallons), '.2f'))
                gallons += 10
        elif choice == POUNDS_TO_KILOGRAMS_CHOICE:
            # Fill the table with values.
            pounds = 0
            for r in range(ROWS):
                values[r][0] = pounds
                values[r][1] = my_conversions.convert_kilograms(pounds)
            # Print the list.
            print('Pounds', '\tKilograms')
            print('-----------------------')
            for r in range(ROWS):
                print(pounds, '     \t', format(my_conversions.convert_kilograms(pounds), '.2f'))
                pounds += 10
        elif choice == INCHES_TO_CENTIMETERS_CHOICE:
            inches = 0
            for r in range(ROWS):
                values[r][0] = inches
                values[r][1] = my_conversions.convert_centimeters(inches)
            # Print the list.
            print('Inches', '\tCentimeters')
            print('--------------------------')
            for r in range(ROWS):
                print(inches, '     \t', format(my_conversions.convert_centimeters(inches), '.2f'))
                inches += 10


# Display the menu.
def display_menu():
    print()
    print('         MENU')
    print('1) Miles to kilometers')
    print('2) Fahrenheit to celsius')
    print('3) Gallons to liters')
    print('4) Pounds to kilograms')
    print('5) Inches to centimeters')
    print('6) Quit')


def main():
    get_values()


if __name__ == "__main__":
    main()
