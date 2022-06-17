hours = int(input())
minutes = int(input())

extra_min = minutes + 15
min_left = extra_min % 60
if extra_min <= 59:
    print(f"{hours}:{extra_min}")
elif extra_min > 59 and hours <= 22 and min_left > 9:
    hours += 1  
    print(f"{hours}:{min_left}")
elif extra_min > 59 and hours <= 22:
    hours += 1  
    print(f"{hours}:0{min_left}")
elif extra_min > 59 and hours == 23 and min_left >= 10:
    hours = 0
    print(f"{hours}:{min_left}")
elif extra_min > 59 and hours == 23:
    hours = 0
    print(f"{hours}:0{min_left}")
