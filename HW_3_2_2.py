# Step 1
beatles = []
print(beatles)

# Step 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(beatles)

# Step 3
add = input("Enter the following members of the band:")
for i in beatles:
    if add == 'Stu Sutcliffe' or 'Pete Best':
        add += i
        beatles.append(add)
    else:
        add = input("Enter the following members of the band:")
        continue
print(beatles)

# Step 4
del beatles[-1, -2]
print(beatles)

# Step 5
beatles.insert(0, 'Ringo Starr')
print(beatles)

print("The Fab", len(beatles))