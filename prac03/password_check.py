min_length = 4

def main():
    password = get_password(min_length)
    print_as_asterisks(password)


def get_password(minimum_length):
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Insufficient amount of characters")
        password = input("Please enter a password of at least {} characters: ".format(minimum_length))
    return password


def print_as_asterisks(sequence):
    print('*' * len(sequence))


main()