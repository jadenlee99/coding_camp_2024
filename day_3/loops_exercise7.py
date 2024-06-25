while True:
    number = int(input('Enter a number below 100: '))

    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    
    if is_prime:
        print(f"{number} is a prime number. Program ends.")
        break
    else:
        print(f'{number} is not a prime number. Please enter another number.')