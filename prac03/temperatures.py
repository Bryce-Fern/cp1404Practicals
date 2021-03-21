"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
         if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = C(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
         elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = F(fahrenheit)
            print("Result: {:.2f} F".format(celsius))
         else:
            print("Invalid option")
         print(MENU)
         choice = input(">>> ").upper()
print("Thank you.")

def F(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def C(celsius):
    return celsius * 9.0 / 5 + 32
main()