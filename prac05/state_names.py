state_name = {"NSW": "New South Wales", "QLD": "Queensland", "NT": "Northern Territory",
              "ACT": "Australian Capital Territory", "VIC": "Victoria", "WA": "Western Australia", "TAS": "Tasmania"}

state = input("Enter abbreviated state name: ").upper()
while state != "":
    if state in state_name:
        print(state, "is", state_name.get(state))
    else:
        print("Invalid State Name")
    state = input("Enter abbreviated state name: ").upper()
