total_guests = int(input())
reservation_numbers = {*()}
arrived_guests = {*()}

for i in range(total_guests):
    reservation_numbers.add(input())

arrival = input()
while arrival != "END":
    arrived_guests.add(arrival)
    arrival = input()

missing_guests = reservation_numbers - arrived_guests
print(len(missing_guests)) 

for guest in sorted(missing_guests):
    print(guest)    