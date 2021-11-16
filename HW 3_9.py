user_word = input("Enter the word:")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        user_word -= letter
    elif letter == "E":
        user_word -= letter
    elif letter == "I":   
        user_word -= letter
    elif letter == "O":   
        user_word -= letter
    elif letter == "U":   
        user_word -= letter
    else:
        break
print(user_word)