import requests
import sys


try:
    amount = float(sys.argv[1])
except KeyError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Error while fetching data from API")
price = price.json()["bpi"]["USD"]["rate_float"]
print(f"${amount*price:,.4f}")
