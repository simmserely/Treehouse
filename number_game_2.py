# generate a random number between 1 and 10
import random

def results(guess, actual):
    # compare guess to secret number
    if guess == actual:
    # print hit/miss
        print('That\'s a HIT! The number was {}. YOU WIN.'.format(actual))
        return True
    else:
    # print 'too low' or 'too high' messages for bad guesses
        if (guess - actual) > 0:
            print('That\'s a MISS! That guess is too high.')
        else:
            print('That\'s a MISS! That guess is too low.')
        return False

# let people play again
def playtime(replay):
    if replay.lower() == 'y':
        game()
    else:
        print('OK. Thanks for playing!')

def game ():
    int_start = 1
    int_end = 10
    actual_no = random.randint(int_start,int_end)
    guesses = []
    # limit the number of guesses
    tries = int_end / 2

    while len(guesses) < tries:
        # get a number guess from the player
        try:
            guess_no = int(raw_input('Guess a number between 1 and 10: '))
        # catch when someone enters a non-integer
        except ValueError:
            print('INVALID ENTRY. You have to enter a figure.')
        else:
            winner = results(guess_no, actual_no)
            guesses.append(guess_no)
            if winner == True:
                break
            elif len(guesses) == tries:
                print('GAME OVER. Your guesses were {}.'.format(guesses))
                replay = raw_input('Would you like to try again? Enter Y/N.')
                playtime(replay)
            else:
                print('TRY AGAIN! You have {} tries left'.format(tries - len(guesses)))

game()
