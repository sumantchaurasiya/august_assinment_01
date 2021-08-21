a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for num in a:
    if num < 5:
        b.append(num)
print(b)

# make a list and take input by user

List = []
Input_List = input('\nEnter all data of list : ')
User_List = Input_List.split(" ")
for data in User_List:
    if data.isdigit():
        int_data = int(data)
        List.append(int_data)
    else:
        List.append(data)
print(List)



