import sys

n = input('Enter n: ')
try:
    n = int(n)
except ValueError:
    print('Invalid input. Please enter a valid integer.')
    sys.exit(1)  # Exit the program with a non-zero status code

if n > 0:
    symbol = '# '
    for i in range(n-1, -1,-1):  # i 2 1 0

        number_of_symbol = n - i
        print((i * " " )+ (number_of_symbol * symbol))
        if symbol == '# ':
            symbol = '$ '
        else:
            symbol = '# '


else:
    print('Try with positive integer')


