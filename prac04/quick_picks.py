
import random

numbers_per_line = 6
min = 1
max = 45

def main():
    quick_picks = int(input("How many quick picks?: "))
    while quick_picks < 0:
        print("That does not work")
        quick_picks = int(input("How many quick picks?: "))

    for n in range(quick_picks):
        quick_pick = []
        for k in range(numbers_per_line):
            number = random.randint(min, max)
            while number in quick_pick:
                number = random.randint(min, max)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()
