list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(list)

for i in range(len(list) - 1):
    if list[i] == list[i + 1]:
        del list[i]

print(list)
