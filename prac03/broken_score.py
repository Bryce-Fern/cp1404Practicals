"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(evaluated_score(score))


def evaluated_score(score):
        if score < 0 or score > 100:
            return "Score is invalid"
        elif score > 50 and score < 90:
            return "Passable"
        elif score > 90 and score <= 100:
            return "Excellent"
        elif score < 50:
            return "Bad"
        else:
            print("Invalid input")

main()