spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
    for item in list[:-2]:
        print(item, end=', ')
    for item in list[-2:-1]:
        print(item, end=' and ')
    for item in list[-1:]:
        print(item, end='.')

comma(spam)


