import inflect

p = inflect.engine()
Names = []
while True:
    try:
        name = input("Name: ")
        Names.append(name)
    except EOFError:
        break
print(f"Adieu, adieu, to {p.join(Names)}")
