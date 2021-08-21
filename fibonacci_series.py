# program of fibonacci series
i, n, n1 = 2, 0, 1
List = [0, 1]
print('Fibonacci Series of First n Number')
num = input('Enter Value of n : ')
if num.isdigit():
    int_num = int(num)
    while i < int_num:
        n2 = n + n1
        List.append(n2)
        n = n1
        n1 = n2
        i += 1
    print(List)
else:
    print('enter integer number '.title())



