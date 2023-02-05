fire_list = input().split("#")
water_amount = int(input())
total_effort = 0
cells_put_out = []
total_fire = 0


for cell in fire_list:
    fire_values = cell.split(" = ")
    type_of_fire = fire_values[0]
    amount_of_fire = int(fire_values[1])
    cell_aproved = False
    if water_amount < amount_of_fire:
        continue
    if type_of_fire == "High":
        if 80 < amount_of_fire <= 125:
            water_amount -= amount_of_fire
            total_effort += 0.25 * amount_of_fire
            cell_aproved = True
    elif type_of_fire == "Medium":
        if 50 < amount_of_fire <= 80:
            water_amount -= amount_of_fire
            total_effort += 0.25 * amount_of_fire
            cell_aproved = True
    elif type_of_fire == "Low":
        if 1 <= amount_of_fire <= 50:
            water_amount -= amount_of_fire
            total_effort += 0.25 * amount_of_fire
            cell_aproved = True
    if cell_aproved:
        cells_put_out.append(amount_of_fire)
        total_fire += int(amount_of_fire)

print("Cells:")
for print_cell in cells_put_out:
    print(f" - {print_cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

        
