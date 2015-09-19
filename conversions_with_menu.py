import my_conversions
# Constants for menu options.
MILES_TO_KILOMETERS_CHOICE = 1
FAHRENHEIT_TO_CELSIUS_CHOICE = 2
GALLONS_TO_LITERS_CHOICE = 3
POUNDS_TO_KILOGRAMS_CHOICE = 4
INCHES_TO_CENTIMETERS_CHOICE = 5
QUIT_CHOICE = 6


def main():
    # Open a file.
    conversions = open('Conversions.txt', 'w')
    conversions.write('Here are some conversions:\n')
    conversions.write('-----------------------------------\n')

    print("This program converts units.")
    print("You will enter a number to get your desired output.")
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        # Get user's choice.
        try:
            choice = int(input('Enter a number from the menu (from 1 to 6): '))
            choice != range(1, 7)
        except ValueError:
            print('Please enter the menu options only!')
        if choice == MILES_TO_KILOMETERS_CHOICE:
            # Perform conversions 10 times for each choice made.
            for count in range(0, choice + 10):
                try:
                    miles = float(input('Enter miles: '))
                    kilometers = my_conversions.convert_kilometers(miles)
                    if miles < 0:
                        print('Please enter a number greater than zero!')
                    else:
                        print('For', miles, 'miles, there are', format(kilometers, '.2f'),
                              'kilometers')
                        # Write to the file.
                        conversions.write(
                            'miles: ' + str(miles) + '    kilometers:  ' + str(kilometers) + '\n')
                except ValueError:
                    print('Please enter a number greater than zero!')
                    print("Invalid input. Please enter numbers only.")
        elif choice == FAHRENHEIT_TO_CELSIUS_CHOICE:
            choice = 0
            for count in range(0, choice + 10):
                try:
                    fahrenheit = float(input('Enter temp: '))
                    celsius = my_conversions.convert_celsius(fahrenheit)
                    if fahrenheit > 1000:
                        print('Enter a number below 1000!')
                    else:
                        print('Your new temp is',
                              format(my_conversions.convert_celsius(fahrenheit), '.2f'),
                              "celsius.")
                        # Write to the file.
                        conversions.write('fahrenheit: ' + str(fahrenheit) + '    celsius: ' + str(celsius) + '\n')
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
        elif choice == GALLONS_TO_LITERS_CHOICE:
            choice = 0
            for count in range(0, choice + 10):
                try:
                    gallons = int(input('Enter a number of gallons: '))
                    liters = my_conversions.convert_liters(gallons)
                    if gallons < 0:
                        print('Enter a number greater than zero!')
                    else:
                        print('The number of gallons is equal to',
                              format(my_conversions.convert_liters(gallons), '.2f'), "liters.")
                        # Write to the file.
                        conversions.write('gallons: ' + str(gallons) + '    liters: ' + str(liters) + '\n')
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

        elif choice == POUNDS_TO_KILOGRAMS_CHOICE:
            choice = 0
            for count in range(0, choice + 10):
                try:
                    pounds = int(input('Enter a number of pounds: '))
                    kilograms = my_conversions.convert_kilograms(pounds)
                    if pounds < 0:
                        print('Please enter a number greater than zero!')
                    else:
                        print('The number of liters is equal to',
                              format(my_conversions.convert_kilograms(pounds), '.2f'),
                              'kilograms.')
                        # Write to the file.
                        conversions.write('pounds: ' + str(pounds) + '    kilograms: ' + str(kilograms) + '\n')
                except ValueError:
                    print('Value entered must be greater than zero!')

        elif choice == INCHES_TO_CENTIMETERS_CHOICE:
            choice = 0
            for count in range(0, choice + 10):
                try:
                    inches = int(input('Enter a number of inches: '))
                    centimeters = my_conversions.convert_centimeters(inches)
                    if inches < 0:
                        print('Please enter a number greater than zero!')
                    else:
                        print('The number of inches is equal to',
                              format(my_conversions.convert_centimeters(inches), '.2f'),
                              'centimeters.')
                        # Write to the file.
                        conversions.write('inches: ' + str(inches) + '    centimeters: ' + str(centimeters) + '\n')
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
        elif choice == QUIT_CHOICE:
            print('Goodbye!')
        else:
            print('Error! Invalid input.')

    conversions.close()


def display_menu():
    print('         MENU')
    print('1) Miles to kilometers')
    print('2) Fahrenheit to celsius')
    print('3) Gallons to liters')
    print('4) Pounds to kilograms')
    print('5) Inches to centimeters')
    print('6) Quit')


main()
