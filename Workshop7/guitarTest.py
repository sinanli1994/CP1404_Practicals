from guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Gibson 2011", 2011, 20000)

print(guitar1.get_age())
print(guitar2.get_age())
print(guitar1.is_vintage())
print(guitar2.is_vintage())

guitars = []
guitars.append(guitar1)
guitars.append(guitar2)

for i, guitar in enumerate(guitars):
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               guitar.is_vintage()))
