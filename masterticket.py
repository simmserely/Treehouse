import sys

TICKET_PRICE = 10
SERVICE_CHARGE = 2
num_tx_left = 100

def calc_price(tx):
    return (tx * TICKET_PRICE) + SERVICE_CHARGE

print('\n\nW E L C O M E    T O    M A S T E R T I C K E T  !')
while num_tx_left > 0:
    print('\nWe have {} ticket/s remaining for our next event.\n'.format(num_tx_left))
    user = input('What name would you like to order under? ')
    print('\nOk, {}.'.format(user), end=' ')
    try:
        num_tx_wanted = int(input('How many tickets would you like? '))
        if num_tx_wanted > num_tx_left:
            raise ValueError('Order size must be less than {}.'.format(num_tx_left))
    except ValueError as err:
        print('Input must be numerical, e.g. 4 (not four).', err, 'Please try again.')
    else:
        amount_due = calc_price(num_tx_wanted)
        print('\nGreat. {} ticket/s will cost you ${}.'.format(num_tx_wanted, amount_due))
        confirm = input('Is that all right with you? Y/N ')
        if confirm.lower() in 'yes':
            num_tx_sold = num_tx_wanted
            num_tx_left -= num_tx_sold
            print('\nSold! Thank you for your purchase. Enjoy yourself!\n')
        else:
            print('\nNo worries. Thanks, {}. Come back if you change your mind!\n'.format(user))

print('\nI\'m sorry!! It looks like we\'re all out of tickets now.')
