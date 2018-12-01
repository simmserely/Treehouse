import random

# make a list of words
word_list = ['apple', 'banana', 'grapes', 'pear']

# pick a random word from list
def word_selector(list):
    word_position = random.randint(0, (len(list)-1))
    return list[word_position]

# draw spaces
def draw_word(word):
    spaces = []
    for n in word:
        spaces.append('_')
    return spaces
    #print('__ ' * len(word))

# take a guess
def game():
    print('Let\'s play HANGMAN! I just picked a random word from a list:')
    word = word_selector(word_list)
    spaces = draw_word(word)
    print spaces
    guess_letter = raw_input('Guess a letter: ')

# draw guessed letters and strikes
# if guessletter is in word
    #then find letter in word, return position
    #use that position to replace space positions with letter
    #print out the updated spaces list

# print out win/lose
    #need to figure out number of tries (length of word)
    # loop the number of user guesses to the number of tries
    # print out negative response if guess is wrong
    # print out number of turns left if guess is wrng
game()
