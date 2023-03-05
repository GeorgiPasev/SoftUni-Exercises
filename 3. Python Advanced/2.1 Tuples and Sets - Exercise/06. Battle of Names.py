N = int(input())
set_odd, set_even = {*()}, {*()}

for i in range(1, N + 1):
    name = input()
    ascii_sum_divide = sum(map(ord, name)) // i
    if ascii_sum_divide % 2 == 1:
        set_odd.add(ascii_sum_divide)
    else:
        set_even.add(ascii_sum_divide)

set_odd_sum, set_even_sum = sum(set_odd), sum(set_even)

if set_odd_sum > set_even_sum:
    result = set_odd - set_even #diff
elif set_odd_sum < set_even_sum:
    result = set_odd ^ set_even #sym_diff
else:
    result = set_odd | set_even #union

print(*result, sep=", ")