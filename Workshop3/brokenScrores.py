def main():
    result = get_result()
    print(result)


def get_result():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"

main()