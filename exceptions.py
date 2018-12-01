try:
    count = int(input('Give me a number '))
except NameError:
    print('That is not a number!')
else:
    print('Hi' * count)
