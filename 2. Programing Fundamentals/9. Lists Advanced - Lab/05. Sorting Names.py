names_list = input().split(', ')
result = sorted(names_list, key=lambda x: (-len(x), x))
print(result)