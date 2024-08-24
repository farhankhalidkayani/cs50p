Expression = input("Expression: ").replace(" ", "").strip()
if "+" in Expression:
    num1, num2 = Expression.split("+")
    print(float(num1)+float(num2))
elif "-" in Expression:
    num1, num2 = Expression.split("-")
    print(float(num1)-float(num2))
elif "*" in Expression:
    num1, num2 = Expression.split("*")
    print(float(num1)*float(num2))
elif "/" in Expression:
    num1, num2 = Expression.split("/")
    print(float(num1)/float(num2))
