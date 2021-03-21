"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score >= 0:
    if score > 100:
        print("Invalid score")
        score = float(input("Please enter valid score: "))
    elif score > 50 and score < 90:
        print("Passable")
        score = float(input("Enter score: "))
    elif score > 90 and score <= 100:
        print("Excellent")
        score = float(input("Enter score: "))
    elif score < 50:
        print("Bad")
        score = float(input("Enter score: "))
else:
    print("Invalid input")