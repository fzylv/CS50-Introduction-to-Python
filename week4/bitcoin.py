import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Please enter a valid number.")

    url = "https://api.coincap.io/v2/assets/bitcoin"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        sys.exit(f"Unable to fetch data from CoinCap API. {e}")

    try:
        data = response.json()
        bitcoin_price = float(data['data']['priceUsd'])
    except (KeyError, ValueError):
        sys.exit("Unable to parse the Bitcoin price from the response.")

    total_cost = bitcoins * bitcoin_price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
