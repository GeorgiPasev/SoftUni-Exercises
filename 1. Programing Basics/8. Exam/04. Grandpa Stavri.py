days = int(input())
total_liters = 0
sum_degrees_per_liter = 0

for day in range(days):
    liters_rakia = float(input())
    degrees_current_bottle = float(input())
    total_liters += liters_rakia
    sum_degrees_per_liter += liters_rakia * degrees_current_bottle

average_degrees = sum_degrees_per_liter / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")