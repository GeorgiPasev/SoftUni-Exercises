lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_broken_counter = 0
sword_broken_counter = 0
shield_broken_counter = 0
armor_broken_counter = 0

for lost_fight in range(1, lost_fights_count + 1):
    helmet_broken = False
    sword_broken = False
    if lost_fight % 2 == 0:
        helmet_broken_counter += 1
        helmet_broken = True
    if lost_fight % 3 == 0:
        sword_broken_counter += 1
        sword_broken = True
    if helmet_broken and sword_broken:
        shield_broken_counter += 1
        if shield_broken_counter % 2 == 0:
            armor_broken_counter += 1

expenses = helmet_broken_counter * helmet_price + sword_broken_counter * sword_price +\
    shield_broken_counter * shield_price + armor_broken_counter * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
    
#Alternative
total_helmets_broken = lost_fights_count // 2
total_swords_broken = lost_fights_count // 3
total_shields_broken = lost_fights_count // 6 # 2 * 3
total_armors_broken = total_shields_broken // 2

expenses = total_helmets_broken * helmet_price + total_swords_broken * sword_price +\
    total_shields_broken * shield_price + total_armors_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

