def add(num1, num2):
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print('ERROR: Input is not a number')
    else:
        print(sum)

total = add('five', 4)
