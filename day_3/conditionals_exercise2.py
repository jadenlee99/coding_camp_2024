number = int(input('Give me a number. '))

if number%2==0 and number <= 7:
    print('It is divisible by 2.')
elif number%2==0 and number > 7:
    print('It is divisible by 2 and the reminder of dividing by 7 is', number%7)
elif number%3==0 and number <= 7:
    print('It is divisible by 3.')
elif number%3==0 and number > 7:
    print('It is divisible by 3 and the reminder of dividing by 7 is', number%7)
elif number > 7:
    print(number%7)
else:
    pass