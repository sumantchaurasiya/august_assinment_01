""" the program is check given number is even or odd and more...."""
y = "yes"
while y == "yes" or y == "y" :
    number = input('Enter a number : ')
    if number.isdigit():
        int_number = int(number)
        even = int_number % 2
        if even == 0:
            print('Given number is "Even number" ')
            divisible_by_four = int_number % 4
            if divisible_by_four == 0:
                print('and also divisible by 4 !')
            else:
                print('But not divisible by 4 !')
        else:
            print('Given number is odd !')
    else:
        print('invalid input , please inter a "number" ')
    Y = input('you want to continue type yes otherwise type any key : ')
    y = Y.lower()