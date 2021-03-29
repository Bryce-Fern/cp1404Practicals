

def main():
    income = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        monthly_income = float(input("Enter income for month {}: ".format(month)))
        income.append(monthly_income)

    print(income_report(income))


def income_report(income):
    print("Income Report")
    total = 0
    for month, income in enumerate(income):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
              Total: $ {}".format(month + 1, income, total))

main()