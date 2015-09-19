# Number Analysis Generator.

NUMBERS = 10

def main():
    # Create a list.
    num = [0] * 10
    index = 0
    # Get input from user.
    for index in range(NUMBERS):
        print('Enter value #', index + 1, ': ', sep='', end='')
        num[index] = int(input())
        index += 1

    # Print the results.
    print('The lowest number is:', min(num))
    print('The highest number is:', max(num))
    print('The total of the numbers is:', sum(num))
    print('The average number is:', sum(num) / float(len(num)))

main()
    
    
