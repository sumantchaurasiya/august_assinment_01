""""take name and age from user"""
y = 'yes'
while (y == 'yes') or (y == 'y'):
    name = input('Enter Name : ')
    age = input('Enter age : ')
    if age.isdigit():
        if not name.isdigit():
            int_age = int(age)
            if (int_age > 0) and (int_age <= 100):
                print(f'Your Name is {name} and Age is {age} years !')
                print(f'after {100 - int_age} years you turn 100 years old !')
            else:
                print('please enter valid age !')
        else:
            print('please enter correct name !')
    else:
        print('please enter correct age')
    y = input('\n Are you want to continue type "yes" or "y" otherwise type "any key" : ')
