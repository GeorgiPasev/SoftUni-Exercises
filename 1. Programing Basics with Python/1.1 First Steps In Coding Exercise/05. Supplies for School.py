pen_pack = int(input())
marker_pack = int(input())
liters_cleaning_agent = float(input())
discount = int(input())
money_base = pen_pack * 5.80 + marker_pack * 7.20 + liters_cleaning_agent * 1.20
money_needed = money_base * (1 - discount/100)
print(money_needed)