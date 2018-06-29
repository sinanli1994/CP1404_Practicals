user_input = input("Please enter the sentence: ")

my_dict = {}
words = user_input.lower().split()


for i in words:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print("Text: ", user_input)

for j in sorted(my_dict):
    print("{:{}} : {}".format(j, 5, my_dict[j]))