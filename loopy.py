items = ['abc', 'def', 'abc', 'efg']

def loopy(item):
    for item in items:
        try:
            if (item.index('a')) == 0:
                continue
        except ValueError:
#            print('Substring not found')
            print(item)

loopy(items)
# print(items.index('abc')== 0)
