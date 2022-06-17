import math

name_of_series = input()
length_of_episode = int(input())
length_of_break = int(input())

lunchtime = length_of_break / 8
chilltime = length_of_break / 4
needed_time = length_of_episode + lunchtime + chilltime
if needed_time <= length_of_break:
    min_left = length_of_break - needed_time
    print(f"You have enough time to watch {name_of_series} and left with {math.ceil(min_left):.0f} minutes free time.")
else:
    min_needed = needed_time - length_of_break
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(min_needed):.0f} more minutes.")