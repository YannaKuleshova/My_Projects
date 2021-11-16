# Read year number
years = int(input("Enter the year number: "))

# Choose the year number
if years%4 != 0:
    print(years, "it's a common year")
elif years%100 != 0:
    print(years, "it's a leap year")
elif years%400 != 0:
    print(years, "it's a common year")
else: 
    print(years, "it's a leap year")

# if  years < 1582:   
#   print("Not within the Gregorian calendar period")
# else:
#   print("Within the Gregorian calendar period")