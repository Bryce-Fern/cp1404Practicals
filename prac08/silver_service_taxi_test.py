from prac08.silver_service_taxi import SSTaxi


def main():
    taxi = SSTaxi("Hummer", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
