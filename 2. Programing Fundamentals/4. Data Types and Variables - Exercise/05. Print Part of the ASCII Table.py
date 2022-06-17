char_start = int(input())
char_end = int(input())

for i in range(char_start, char_end + 1):
    print(chr(i), end=" ")

#Alternative
# final_string = ''
# final_string += chr(i) + " " #inside the loop

# print(final_string)
# print(final_string[0:-1]) # using slicing to remove the last interval \
                            # if needed