n, m = map(int, input().split())
set_1, set_2 = {*()}, {*()}

for i in range(n):
    set_1.add(int(input()))

for i in range(m):
    set_2.add(int(input()))

set_3 = set_1 & set_2

print(*set_3, sep="\n")

# for element in set_1 & set_2:
#     print(element)
