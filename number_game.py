import random

# generate a random number between 1 and 10
actual_no = random.randint(1,10)

# compare guess to secret number
def compare(guess, actual):
   return guess == actual

# print hit/miss
def results(comparison):
    if comparison == True:
        print('That\'s a HIT! The number was {} YOU WIN.'.format(actual_no))
    else:
        print('That\'s a MISS! Try again!')

# get a number guess from the player
while True:
    guess_no = int(raw_input('Guess a number between 1 and 10: '))
    comparison = compare(guess_no, actual_no)
    results(comparison)
    if comparison == True:
        break
