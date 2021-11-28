#########################
#Author: Kuleshova Yana
#Date: 27/11/2021
#Task: CW to L7_1
#########################

word = 'by'
print(len(word))

empty = ''
print(len(empty))

#
multiline = '''Line #1
Line2'''
print(len(multiline))

multiline1 = '''Line #1
Line2'''
print(len(multiline1))

#
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#
char_1 = 'a'
char_2 = ' '
print(ord(char_1))
print(ord(char_2))

#
x = 'a'
x1 = 97
print(type(x))
print(type(ord(x)))
print(type(chr(x1)))

print(chr(ord(x)), x)
print(chr(ord(x)) == x)

print(ord(chr(x1)), x1)
print(ord(chr(x1)) == x1)

# Indexing string

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end = ' ')

print()

#
the_string = 'silly walks'

for ix in range(len(the_string)-1, -1, -1):
    print(the_string[ix], end = ' ')

print()

#
the_string = 'silly walks'

for character in the_string:
    print(character, end = '\n')

print()

# Slices
alpha = 'abdefg'

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# The in operator
alphabet = 'abdefgerxtcyvukjhgfKilukyjthr'

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyu" in alphabet)

# The not in operator
alphabet = 'abdefgerxtcyvukjhgfKilukyjthr'

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyu" not in alphabet)

# Operations on strings: continued
alphabet = 'abdefgerxtcyvukjhgfKilukyjthr'

alphabet = 'a' + alphabet
alphabet = alphabet + 'z'

print(alphabet)

# Operations on strings: min()
print(min('aAbByzZ'))

t = 'The knights Who Say "Ni!"'
print('[' + min(t) + ']')

space = min(t)
print("is a space:", "\"", space, "\"", sep = "")
print(ord(space))
print()

t = [0, 1, 2]
print(min(t))

# Operations on strings: max()
print(max('aAbByzZ'))

t = 'The knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Operations on strings: the index() method
print("aAbByzZaA".index("b") + 1)
print("aAbByzZaA".index("Z") + 1)
print("aAbByzZaA".index("A") + 1)

# Operations on strings: the list() function
st = "abcaba"
print(st, type(st), list(st))
print()

di = {1: "1", 2: "2"}
print(di, type(di), list(di))
print()

tupl1 = ("1", "2")
print(tupl1, type(tupl1), list(tupl1))

# Exercises
s = '"'
print(len(s))

s = 'yesteryears'
the_list = list(s)
print(the_list[3:6])

for ch in "abc":
    print(chr(ord(ch) + 1), end = '')

