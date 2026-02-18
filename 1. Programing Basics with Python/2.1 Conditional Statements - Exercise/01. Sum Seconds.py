contestant_time_1 = int(input())
contestant_time_2 = int(input())
contestant_time_3 = int(input())

time_of_all_contestants = contestant_time_1 + contestant_time_2 + contestant_time_3
whole_minutes = time_of_all_contestants // 60
seconds_left = time_of_all_contestants / 60 - whole_minutes
seconds_left_conversion = seconds_left * 60
# last 2 lines ^ can just be converted by
# time_of_all_contestants % 60 which is the remainder of seconds
# past the decimal point

if 0 <= seconds_left_conversion <= 9:
    print(f"{whole_minutes}:0{seconds_left_conversion:.0f}")
else:
    print(f"{whole_minutes}:{seconds_left_conversion:.0f}")