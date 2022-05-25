username = input()
password = input()

user_input = input()

while user_input != password:
    user_input = input()
else:
    print(f"Welcome {username}!")