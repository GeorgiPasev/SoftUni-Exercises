first_sequence = input().split(', ')
second_sequence = input().split(', ')
substrings = []

for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:# and not first_word in substrings: #alternative way
            substrings.append(first_word)
            break #saves on iterations

print(substrings)

# #comprehension
# first_sequence = input().split(', ')
# second_sequence = input().split(', ')
# substrings = [x for x in first_sequence if any(x in w for w in second_sequence)]
# print(substrings)

# # x - first_word
# # w - second_word