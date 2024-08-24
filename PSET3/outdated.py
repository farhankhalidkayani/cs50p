months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date:").strip()
        if date[0].isdigit():
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
            if d > 31 or m > 12:
                raise ValueError
            res = f"{y}-{m:02}-{d:02}"
        if date[0].isalpha():
            m, d, y = date.split(" ")
            if d[-1] != ',':
                raise ValueError
            d = int(d.strip(","))
            for i, n in enumerate(months):
                if n == m:
                    m = i+1
                    break
            if d > 31 or m > 12:
                raise ValueError
            res = f"{y}-{m:02}-{d:02}"
    except:
        pass
    else:
        break
print(res)
