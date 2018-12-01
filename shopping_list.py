# make a list to hold on to our items
shopping_list = []

# print out instructions on how to use the app
#print('Let\'s create a shopping list.')
#print('Enter "Done" when you are finished adding items.')
#print(shopping_list)

# HELP command to show help message about functions
def help(item):
    if item.lower() == "help":
        print('''
        The DONE command completes your shopping list
        The SHOW command prints out your current shopping list
        This HELP command explains all functions
        ''')

# show command to see all items on the list
def show(item):
    if item.lower() == 'show':
        print('Here is your current list:')
        for item in shopping_list:
            print(item)

# ask for new items
while True:
    new_item = raw_input('Add an item > ')
    show(new_item)
    help(new_item)
# be able to quit the app
    if new_item.lower() == 'done':
        break
# add new items to our list
    if new_item == 'help':
        continue
    elif new_item == 'show':
        continue
    shopping_list.append(new_item)

# print out the list
print
print('Here is your final shopping list:')
for item in shopping_list:
    print(item)
print
