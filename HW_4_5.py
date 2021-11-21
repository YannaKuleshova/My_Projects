def is_prime():
    x = int(input("Введите число: "))
    if x // 2 == 1 or x // 3 == 1 or x // 5 == 1 or x // 7 == 1:
        return True
    else: 
        return False

is_prime()

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end = "")
print()
