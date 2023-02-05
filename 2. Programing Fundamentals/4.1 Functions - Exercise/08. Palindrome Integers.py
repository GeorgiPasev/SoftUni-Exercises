def if_palindrome(list_of_integers):
    for i in list_of_integers:
        if i == i[::-1]:
            print(True)
        else:
            print(False)

list_of_integers = input().split(', ')
if_palindrome(list_of_integers)