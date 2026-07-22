def first_last_characters(word):
    a = word[0:2]
    b = word[-2:]
    return a+b
chosen = input("Enter your word : ")
x = first_last_characters(chosen)
print(x)
