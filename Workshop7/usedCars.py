from Car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    limo = Car(100, "limo")
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)


main()
