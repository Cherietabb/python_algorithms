# using conversions with a custom module.

import my_conversions

# Explain what the program does.
def main():
    print("This program converts units.")
    print("Please enter a number to be converted.")
    if not MilesToKm():
        return False
    if not FahToCel():
        return False
    if not GalToLit():
        return False
    if not PoundsToKg():
        return False
    if not InchesToCm():
        return False


# Define miles to kilometers.
def MilesToKm():
    i = 0
    while i < 3:
        miles = int(input('Enter a number for miles: '))
        if miles < 0:
            print("Value entered must be greater than zero!")
            i += 1
        else:
            print('For every mile, there are', format(my_conversions.kilometers(miles), '.2f'), 'kilometers')
            return True
    print("Too many tries! Program ending...")
    return False


# Convert fahrenheit to celsius.
def FahToCel():
    i = 0
    while i < 3:
        fahrenheit = int(input('Enter a temp: '))
        if fahrenheit > 1000:
            print('Value entered must be less than 1000!')
            i += 1
        else:
            print('Your new temp is', format(my_conversions.celsius(fahrenheit), '.2f'), "celsius.")
            return True
    print('Too many tries! Program ending...')
    return False


# Convert gallons to liters.
def GalToLit():
    i = 0
    while i < 3:
        gallons = int(input('Enter a number of gallons: '))
        if gallons < 0:
            print('Value entered must be greater than zero!')
            i += 1
        else:
            print('The number of gallons is equal to', format(my_conversions.liters(gallons), '.2f'), "liters.")
            return True
    print('Too many tries! Program ending...')
    return False


# Convert pounds to kilograms.
def PoundsToKg():
    i = 0
    while i < 3:
        pounds = int(input('Enter a number of pounds: '))
        if pounds < 0:
            print('Value entered must be greater than zero!')
            i += 1
        else:
            print('The number of liters is equal to', format(my_conversions.kilograms(pounds), '.2f'), 'kilograms.')
            return True
    print('Too many tries! Program ending...')
    return False


# Convert inches to centimeters
def InchesToCm():
    i = 0
    while i < 3:
        inches = int(input('Enter a number of inches: '))
        if inches < 0:
            print('Value entered must be greater than zero!')
            i += 1
        else:
            print('The number of inches is equal to', format(my_conversions.centimeters(inches), '.2f'), 'centimeters.')
            return True
    print('Too many tries! Program ending...')
    return False

# Call main function.
main()
