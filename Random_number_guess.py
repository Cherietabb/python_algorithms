# Generate a random number between 1 and 1000.
import random


def main():
    number = random.randint(1, 1000)
    play_again = 'y'
    tries = 0
    tries += 1
    while play_again == 'y':
        guess = int(input('Guess a number between 1 and 1000: '))
        tries += 1
        if guess > number:
            if guess - number < 10:
                print('Getting warmer, but still too high!')
            else:
                print('Too high!')
        elif guess < number:
            if number - guess <= 10:
                print('Getting warmer, but still too low!')
            else:
                print('Too low!')
        else:
            print("You're on a roll! You got the correct number in", tries, "guesses!")
            play_again = input("Play again? (Enter 'y' for yes): ")
    else:
        print("Thank you for playing. Goodbye!")


main()
