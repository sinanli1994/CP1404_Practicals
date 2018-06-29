import random

MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
day = 1

price = INITIAL_PRICE
print("On day 1 price is: ${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    day += 1
    print("On day {} price is: ${:,.2f}".format(day, price))




