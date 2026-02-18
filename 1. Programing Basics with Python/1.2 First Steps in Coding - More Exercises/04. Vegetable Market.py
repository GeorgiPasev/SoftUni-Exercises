vegetables_price_kg = float(input())
fruits_price_kg = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

total_lv = vegetables_kg * vegetables_price_kg +\
    fruits_kg * fruits_price_kg

total_euro = total_lv / 1.94
print(f"{total_euro:.2f}")