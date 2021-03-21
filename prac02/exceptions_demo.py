try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator


while denominator == 0:
        denominator = int(input("Enter a valid denominator: "))
    else:
        print(fraction)


except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Q.1 Occurs when anything other than an integer is entered as a value.
#Q.2 Occurs when 0 is entered as the denominator
#Q.3 Ask to re-enter a number other than zero