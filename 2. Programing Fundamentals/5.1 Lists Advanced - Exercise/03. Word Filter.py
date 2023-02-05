words = input().split()
filetered_words = [word for word in words if len(word) % 2 == 0]
print('\n'.join(filetered_words))