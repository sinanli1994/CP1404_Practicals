import random

num_of_picks = int(input("Enter number of picks:"))

for i in range(num_of_picks):
    num_list = []
    for j in range(0, 6):
        ran_num = random.randint(1, 46)
        while ran_num in num_list:
            ran_num = random.randint(1, 46)
        num_list.append(ran_num)
    num_list.sort()
    print(num_list)