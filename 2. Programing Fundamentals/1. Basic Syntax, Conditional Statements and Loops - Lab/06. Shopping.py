budget = int(input())
command_buy = input()

while command_buy != "End":
    budget -= int(command_buy)
    if budget < 0:
        print("You went in overdraft!")
        break
    command_buy = input()
else:
    print("You bought everything needed.")