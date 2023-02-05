def loading_bar(number):
    bar = []
    number_to_append = int(number / 10)
    second_number_to_append = 10 - number_to_append
    for char in range(number_to_append):
        bar.append('%')
    for char in range(second_number_to_append):
        bar.append('.')
    bar.append(']')
    bar.insert(0, '[')

    if number_to_append == 10:
        print('100% Complete!')
        print(f'{"".join(bar)}') 
    else:
        print(f"{number_to_append}0%", end=f' {"".join(bar)}')
        print()
        print('Still loading...')

number = int(input())
loading_bar(number)

#alternative
def check_progress(bar_current_value):
    if bar_current_value == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{bar_current_value}% [{'%' * (bar_current_value // 10)}{'.' * (10 - bar_current_value // 10)}]\nStill loading..."

    
bar_value = int(input())
print(check_progress(bar_value))