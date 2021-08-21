
List = []
Input = input('Enter number : ')
if Input.isdigit():
    Int = int(Input)
    for x in range(1, Int+1):
        Remainder = Int % x
        if Remainder == 0:
            List.append(x)
print(List)
