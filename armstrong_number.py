# program of Armstrong number
num = input('enter number :'.title())
armstrong_number = 0
if num.isdigit():
    int_num = int(num)
    len_num = len(num)
    for digit in num:
        armstrong_number = armstrong_number + (int(digit) ** len_num)
    print('Sum of given number digit is '.title(), armstrong_number)
    if armstrong_number == int_num:
        print('so it is armstrong number'.title())
    else:
        print('so it is not an armstrong number'.title())

else:
    print('enter valid number'.title())
