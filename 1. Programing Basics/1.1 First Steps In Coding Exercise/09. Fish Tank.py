lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

parallelepiped_volume = lenght_cm * width_cm * height_cm
parallelepiped_volume *= 1 - percent/100
liters_needed = parallelepiped_volume * 0.001
print(liters_needed)