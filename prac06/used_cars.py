from prac06.car import Car


def main():

    limo = Car("Limo", 100)
    print(limo.car)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)

main()
