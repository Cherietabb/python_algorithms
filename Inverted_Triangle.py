# Inverted triangle using loops


BASE_SIZE = 10

for r in reversed(range(BASE_SIZE)):
    for c in range(r + 1):
        print('*', end='')
    print('')
