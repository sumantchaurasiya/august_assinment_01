y = 'yes'
while y == 'yes' or y == 'y':
    print('palindrome checker program ')
    Input_string = input('Enter a word : ')
    Reverse_string = Input_string[::-1]
    if Input_string == Reverse_string:
        print('Entered word is Palindrome')
    else:
        print('Entered word is not palindrome')
    Y = input('are you want to continue type yes otherwise type any key ')
    y = Y.lower()

