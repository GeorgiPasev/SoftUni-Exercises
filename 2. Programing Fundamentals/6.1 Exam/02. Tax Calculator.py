list_vehicles = input().split('>>')
total_tax_collected = 0

for vehicle in list_vehicles:
    tax = 0
    vehicle_values = vehicle.split()
    car_type = vehicle_values[0]
    years_tax_should_be_paid = int(vehicle_values[1])
    km_travelled = int(vehicle_values[2])
    if car_type == 'family':
        tax_for_km = km_travelled // 3000
        tax += tax_for_km * 12 + (50 - years_tax_should_be_paid * 5)
    elif car_type == 'heavyDuty':
        tax_for_km = km_travelled // 9000
        tax += tax_for_km * 14 + (80 - years_tax_should_be_paid * 8)
    elif car_type == 'sports':
        tax_for_km = km_travelled // 2000
        tax += tax_for_km * 18 + (100 - years_tax_should_be_paid * 9)
    else:
        print("Invalid car type.")
        continue
    print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
    total_tax_collected += tax

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")