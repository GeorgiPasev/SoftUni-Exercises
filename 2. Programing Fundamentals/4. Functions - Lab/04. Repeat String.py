repeat_string = lambda a, b: a * b

string = input()
counter = int(input())
result = repeat_string(string, counter)
print(result)

#Alternative
def repeat_string(a, b):
    return a * b

string = input()
counter = int(input())
result = repeat_string(string, counter)
print(result)