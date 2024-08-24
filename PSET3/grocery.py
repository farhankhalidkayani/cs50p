
List = {}
while True:
    try:
        item = input().upper()
        if item in List:
            List[item] += 1
        else:
            List[item] = 1
    except EOFError:
        break
keys = list(List.keys())
keys.sort()
for key in keys:
    print(f"{List[key]} {key}")
