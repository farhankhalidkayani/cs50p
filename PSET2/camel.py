camel = input("Camel Case: ")
res = ""
for letter in camel:
    if letter == letter.upper():
        res += "_"+letter.lower()
    else:
        res += letter
print(f"Snake Case: {res}")
