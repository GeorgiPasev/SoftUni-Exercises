nylon_needed = int(input())
paint_needed = int(input())
paint_thinner_needed = int(input())
work_in_hours = int(input())

materials_needed = nylon_needed * 1.5 + paint_needed * 14.5 + \
    paint_thinner_needed * 5
extra_materials = paint_needed * 14.5 * 10/100 + 2 * 1.5 + 0.4
expenses = materials_needed + extra_materials + \
    (materials_needed + extra_materials) * 30/100 * work_in_hours
print(expenses)