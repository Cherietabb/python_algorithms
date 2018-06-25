__author__ = 'Cherie Tabb'

import pet


def make_list():
    pet_list = []
    for count in range(1, 2):
        name = input("Enter your pet's name: ")
        animal_type = input("What pet_type of pet is it: ")
        age = int(input('Enter the age of your pet: '))

        new_pet = pet.Pet(name, animal_type, age)
        pet_list.append(new_pet)
    return pet_list


def display_list(pet_list):
    for item in pet_list:
        print('')
        print(item.get_name())
        print(item.get_animal_type())
        print(item.get_age())


def main():
    # Create an empty list.
    pets = make_list()
    print('')
    print('Here are the pets you listed: ')
    display_list(pets)


if __name__ == "__main__":
    main()
