import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

slow_down_time = math.floor(distance_in_meters / 15) * 12.5 
# can also use distance_in_meters // 15 instead of floor
ivan_time = distance_in_meters * time_in_seconds + slow_down_time

if ivan_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    too_slow = ivan_time - record_in_seconds
    print(f"No, he failed! He was {too_slow:.2f} seconds slower.")