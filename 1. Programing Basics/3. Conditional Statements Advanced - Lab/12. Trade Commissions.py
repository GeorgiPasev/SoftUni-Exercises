town = input()
volume_of_sales = float(input())

commission = 0
if town == "Sofia":
    if 0 <= volume_of_sales <= 500:
        commission = 0.05
    elif 500 <= volume_of_sales <= 1000:
        commission = 0.07
    elif 1000 <= volume_of_sales <= 10000:
        commission = 0.08
    elif 10000 < volume_of_sales:
        commission = 0.12
elif town == "Varna":
    if 0 <= volume_of_sales <= 500:
        commission = 0.045
    elif 500 <= volume_of_sales <= 1000:
        commission = 0.075
    elif 1000 <= volume_of_sales <= 10000:
        commission = 0.1
    elif 10000 < volume_of_sales:
        commission = 0.13
elif town == "Plovdiv":
    if 0 <= volume_of_sales <= 500:
        commission = 0.055
    elif 500 <= volume_of_sales <= 1000:
        commission = 0.08
    elif 1000 <= volume_of_sales <= 10000:
        commission = 0.12
    elif 10000 < volume_of_sales:
        commission = 0.145

commission_in_lv = commission * volume_of_sales

if not (town == "Sofia" or "Varna" or "Plovdiv") or commission_in_lv == 0:
    print("error")
else:
    print(f"{commission_in_lv:.2f}")