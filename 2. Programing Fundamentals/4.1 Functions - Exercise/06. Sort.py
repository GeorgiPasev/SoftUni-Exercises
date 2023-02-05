# list_of_integers = [int(i) for i in input().split()]
list_of_integers = list(map(int, input().split()))
# list_of_integers.sort()
# print(list_of_integers)
new_list = sorted(list_of_integers)
print(new_list)