user_name = input("Please enter your name :")

if user_name == "":
    print("Invalid name")
    user_name = input("Please enter your name :")

character = len(user_name)

i = 0

for i in range(1, character, 2):
    print(user_name[i])

