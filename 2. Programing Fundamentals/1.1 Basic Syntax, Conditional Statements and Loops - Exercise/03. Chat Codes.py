number_of_inputs = int(input())

for i in range(number_of_inputs):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")