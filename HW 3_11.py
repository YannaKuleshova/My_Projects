
cO = 153

while cO != 1:
    if cO == 1:
        continue
    
    if cO%2 == 0:
        cO /= 2
        print(int(cO))
    else:
        cO = 3 * cO + 1
        print(int(cO))
else:
    print(int(cO))
