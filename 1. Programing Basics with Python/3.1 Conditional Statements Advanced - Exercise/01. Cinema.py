projection_type = input()
rows = int(input())
columns = int(input())

full_hall = rows * columns
price = 0
if projection_type == "Premiere":
    price = 12
elif projection_type == "Normal":
    price = 7.5
elif projection_type == "Discount":
    price = 5

final_price = full_hall * price 
print(f"{final_price:.2f}")
