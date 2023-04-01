from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))
doll = 0
train = 0
bicycle = 0
bear = 0

toys = {
    'Doll': {
        'magic': 150,
        'crafted': 0
    },
    'Wooden train': {
        'magic': 250,
        'crafted': 0
    },
    'Teddy bear': {
        'magic': 300,
        'crafted': 0
    },
    'Bicycle': {
        'magic': 400,
        'crafted': 0
    }
}

while materials and magic:
    product = materials[-1] * magic[0]
    if product == toys['Doll']['magic']:
        toys['Doll']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Wooden train']['magic']:
        toys['Wooden train']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Teddy bear']['magic']:
        toys['Teddy bear']['crafted'] += 1
        materials.pop()
        magic.popleft()
    elif product == toys['Bicycle']['magic']:
        toys['Bicycle']['crafted'] += 1
        materials.pop()
        magic.popleft()
    else:
        if product < 0:
            materials.append(materials.pop() + magic.popleft())
        elif product > 0:
            materials[-1] += 15
            magic.popleft()
        elif product == 0:
            if materials[-1] == 0:
                materials.pop()
            if magic[0] == 0:
                magic.popleft()

if toys['Doll']['crafted'] > 0 and toys['Wooden train']['crafted'] > 0 or \
    toys['Teddy bear']['crafted'] > 0 and toys['Bicycle']['crafted'] > 0:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(map(str, reversed(materials)))}')
if magic:
    print(f'Magic left: {", ".join(map(str, magic))}')

for toy in sorted(toys):
    if toys[toy]['crafted'] > 0:
        print(f'{toy}: {toys[toy]["crafted"]}')