import re

data = input()

pattern = r'(\@+|\#+)([a-z]{3,})(\@+|\#+)([^A-Za-z0-9]*)(\/[0-9][0-9]*\/)'
result = re.finditer(pattern, data)

green_amount = 0
red_amount = 0
purple_amount = 0


for res in result:
    word = res.group()
    if 'green' in word:
        word = res.group().split('/')
        for i in word:
            if i == '':
                word.remove('')
        if word[1].isdigit():
            amount = word[1]
        print(f"You found {amount} green eggs!")      
    if 'red' in word:
        word = res.group().split('/')
        for i in word:
            if i == '':
                word.remove('')
        if word[1].isdigit():
            amount = word[1]
        elif word[2].isdigit():
            amount = word[2]
        print(f"You found {amount} red eggs!")
    if 'purple' in word:
        word = res.group().split('/')
        for i in word:
            if i == '':
                word.remove('')
        if word[1].isdigit():
            amount = word[1]
        print(f"You found {amount} purple eggs!")