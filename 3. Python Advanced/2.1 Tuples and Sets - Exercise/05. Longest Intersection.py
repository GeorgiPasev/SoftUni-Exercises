N = int(input())
longest_intersection = []


for i in range(N):
    range_1, range_2 = input().split("-")
    range_1 = tuple(map(int, range_1.split(",")))
    range_2 = tuple(map(int, range_2.split(",")))
    range_1 = set(range(range_1[0], range_1[1] + 1))
    range_2 = set(range(range_2[0], range_2[1] + 1))
    intersection = range_1 & range_2
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {*longest_intersection,} with length {len(longest_intersection)}")

#alt
N = int(input())
longest_intersection = {}

for i in range(N):
    left_range, right_range = input().split("-")
    left_range_start_idx, left_range_end_idx = map(int, left_range.split(","))
    right_range_start_idx, right_range_end_idx = map(int, right_range.split(","))
    left_set = set(range(left_range_start_idx, left_range_end_idx + 1))
    right_set = set(range(right_range_start_idx, right_range_end_idx + 1))
    intersection = left_set & right_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")



