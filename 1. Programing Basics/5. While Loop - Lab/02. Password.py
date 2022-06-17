create_username = input()
create_password = input()
password = input()

while password != create_password:
    password = input()

print(f"Welcome {create_username}!")