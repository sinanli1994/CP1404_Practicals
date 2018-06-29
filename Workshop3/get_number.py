def main():
    lower = 10
    upper = 50

    num = get_number(lower, upper)
    print("{} {:>5}".format(num, chr(num)))


def get_number(lower, upper):
    while True:
        try:
            num = int(input("Enter a number ({0}-{1}):".format(lower, upper)))
        except ValueError:
            print("Please enter a valid number!")
        else:
            if num < lower or num > upper:
                print("Please enter a valid number!")
            else:
                break

    return num


main()