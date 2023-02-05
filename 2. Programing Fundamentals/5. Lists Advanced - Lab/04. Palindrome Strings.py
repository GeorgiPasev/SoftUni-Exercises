list_of_palindromes = [pal for pal in input().split() if pal == pal[::-1]]

palindrome_name = input()
counter = list_of_palindromes.count(palindrome_name)
print(list_of_palindromes)
print(f"Found palindrome {counter} times")