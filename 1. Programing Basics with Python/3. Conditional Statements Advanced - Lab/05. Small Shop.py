product = input()
town = input()
amount = float(input())

if town == "Sofia":
    if product == "coffee":
        print(amount * 0.5)
    elif product == "water":
        print(amount * 0.8)
    elif product == "beer":
        print(amount * 1.2)
    elif product == "sweets":
        print(amount * 1.45)
    elif product == "peanuts":
        print(amount * 1.6)
elif town == "Plovdiv":
    if product == "coffee":
        print(amount * 0.4)
    elif product == "water":
        print(amount * 0.7)
    elif product == "beer":
        print(amount * 1.15)
    elif product == "sweets":
        print(amount * 1.3)
    elif product == "peanuts":
        print(amount * 1.5)
elif town == "Varna":
    if product == "coffee":
        print(amount * 0.45)
    elif product == "water":
        print(amount * 0.7)
    elif product == "beer":
        print(amount * 1.1)
    elif product == "sweets":
        print(amount * 1.35)
    elif product == "peanuts":
        print(amount * 1.55)