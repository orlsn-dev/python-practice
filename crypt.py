import argparse
import requests

# Map short tickers to CoinGecko's IDs
TICKERS = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana",
    "doge": "dogecoin",
    "ada": "cardano",
    "xrp": "ripple",
    "ltc": "litecoin",
    "dot": "polkadot",
    "link": "chainlink",
    "matic": "matic-network",
}

parser = argparse.ArgumentParser(description="Check live crypto prices.")
parser.add_argument("coins", nargs="+", help="Tickers like btc eth sol")
args = parser.parse_args()

# Convert tickers to CoinGecko IDs, skip unknown ones
coin_ids = []
unknown = []
for ticker in args.coins:
    ticker = ticker.lower()
    if ticker in TICKERS:
        coin_ids.append(TICKERS[ticker])
    else:
        unknown.append(ticker)

if unknown:
    print(f"Unknown tickers (skipped): {', '.join(unknown)}")

if not coin_ids:
    print("No valid coins to check. Try: btc, eth, sol, doge, ada, xrp, ltc, dot, link, matic")
    exit()

# Fetch prices
ids = ",".join(coin_ids)
url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
response = requests.get(url)
data = response.json()

# Print table
print()
print(f"{'COIN':<12} {'PRICE (USD)':>15}")
print("-" * 28)

for coin in coin_ids:
    price = data[coin]["usd"]
    print(f"{coin.capitalize():<12} ${price:>14,.2f}")

print()