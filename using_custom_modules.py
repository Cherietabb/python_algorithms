# using conversions with a custom module.

import my_conversions


# Define miles to kilometers.
def miles_to_km():
    i = 0
    while i < 3:
        miles = int(input('Enter a number for miles: '))
        if miles < 0:
            print("Value entered must be greater than zero!")
            i += 1
        else:
            print('For every mile, there are', format(my_conversions.convert_kilometers(miles), '.2f'), 'kilometers')
            return True
    print("Too many tries! Program ending...")
    return False


# Convert fahrenheit to celsius.
def f_to_c():
    i = 0
    while i < 3:
        fahrenheit = int(input('Enter a temp: '))
        if fahrenheit > 1000:
            print('Value entered must be less than 1000!')
            i += 1
        else:
            print('Your new temp is', format(my_conversions.convert_celsius(fahrenheit), '.2f'), "celsius.")
            return True
    print('Too many tries! Program ending...')
    return False


# Convert gallons to liters.
def gal_to_lit():
    i = 0
    while i < 3:
        gallons = int(input('Enter a number of gallons: '))
        if gallons < 0:
            print('Value entered must be greater than zero!')
            i += 1
        else:
            print('The number of gallons is equal to', format(my_conversions.convert_liters(gallons), '.2f'), "liters.")
            return True
    print('Too many tries! Program ending...')
    return False


# Convert pounds to kilograms.
def lbs_to_kg():
    i = 0
    while i < 3:
        pounds = int(input('Enter a number of pounds: '))
        if pounds < 0:
            print('Value entered must be greater than zero!')
            i += 1
        else:
            print('The number of liters is equal to', format(my_conversions.convert_kilograms(pounds), '.2f'),
                  'kilograms.')
            return True
    print('Too many tries! Program ending...')
    return False


# Convert inches to centimeters
def in_to_cm():
    i = 0
    while i < 3:
        inches = int(input('Enter a number of inches: '))
        if inches < 0:
            print('Value entered must be greater than zero!')
            i += 1
        else:
            print('The number of inches is equal to', format(my_conversions.convert_centimeters(inches), '.2f'),
                  'centimeters.')
            return True
    print('Too many tries! Program ending...')
    return False


# Call main function.
def main():
    # Explain what the program does.
    print("This program converts units.")
    print("Please enter a number to be converted.")
    if not miles_to_km():
        return False
    if not f_to_c():
        return False
    if not gal_to_lit():
        return False
    if not lbs_to_kg():
        return False
    if not in_to_cm():
        return False


if __name__ == "__main__":
    main()
