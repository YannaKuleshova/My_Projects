# Input the income.
income = int(input("Enter the income: "))

if income == 0:
    print(input("Enter the income > 0: "))
else:
    income *= 0.15
print("Your tax: ", income)