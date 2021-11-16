amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount*0.05
    print("Doscount", discount)
else:
    discount = amount*0.10
    print("Discount", discount)

print("Next payabel: ", amount - discount)