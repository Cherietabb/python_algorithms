# Lottery number Generator.

import random

# Constant
NUM = 7


def get_lottery_numbers():
    # Create empty list to hold numbers.
    lottery_numbers = [0] * NUM
    index = 0
    # Get lottery numbers
    while index < len(lottery_numbers):
        lottery_numbers[index] = random.randint(1, 10)
        index += 1
    print('Winning Lottery Numbers')
    print('-----------------------')
    display_list(lottery_numbers)


def display_list(lottery_numbers):
    for value in lottery_numbers:
        print(value)


def main():
    get_lottery_numbers()


if __name__ == "__main__":
    main()
