def hows_the_parrot():
    print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name):
    if name.lower() == 'kenneth':
        print('Kenneth\'s a lumberjack and he\'s OK!')
    else:
        print('{} sleeps all night and {} works all day'.format(name, name))

def lumberjack2(name, pronoun):
    print('{}\'s a lumberjack and {} OK!'.format(name, pronoun))

lumberjack('Nancy')
lumberjack2('Kenneth', 'he\'s')

def average(num1, num2):
    return (num1 + num2) / 2
    
avg = average(2, 8)
print(avg)
