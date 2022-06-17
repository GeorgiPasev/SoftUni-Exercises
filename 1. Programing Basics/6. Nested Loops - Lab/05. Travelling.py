destination = input()

while destination != "End":
    min_budget = float(input())
    sum_saved = 0
    while sum_saved < min_budget:
        money_saved = float(input())
        sum_saved += money_saved
    print(f"Going to {destination}!")
    destination = input()
