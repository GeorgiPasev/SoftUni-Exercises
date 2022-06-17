hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

time_of_exam = hour_of_exam * 60 + minute_of_exam
time_of_arrival = hour_of_arrival * 60 + minute_of_arrival

if time_of_arrival > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print("On time")
else:
    print("Early")

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    difference = time_of_exam - time_of_arrival
    print(f"{difference} minutes before the start")
elif time_of_arrival <= time_of_exam - 60:
    difference = time_of_exam - time_of_arrival
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours before the start")
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    difference = time_of_arrival - time_of_exam
    print(f"{difference} minutes after the start")
elif time_of_arrival >= time_of_exam + 60:
    difference = time_of_arrival - time_of_exam
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours after the start")
