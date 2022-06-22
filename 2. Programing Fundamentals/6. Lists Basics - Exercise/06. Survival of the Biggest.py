list_of_integers = input().split()
count_to_remove = int(input())

for i in range(len(list_of_integers)):#converting strings in list to int
    list_of_integers[i] = int(list_of_integers[i])
    #or can append it to another list

for i in range(count_to_remove):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)

for i in range(len(list_of_integers)):
    list_of_integers[i] = str(list_of_integers[i])

print(", ".join(list_of_integers))
