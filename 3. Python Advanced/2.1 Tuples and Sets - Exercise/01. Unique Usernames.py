n = int(input())
usernames = {*()}

for i in range(n):
    usernames.add(input())

print(*usernames, sep="\n")