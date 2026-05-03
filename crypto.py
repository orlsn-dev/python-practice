import argparse
import time
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
parser.add_argument("--watch", type=int, metavar="SECONDS", help="Auto-refresh every N seconds")
parser.add_argument("--alert", action="append", metavar="TICKER:PRICE", help="Alert when price crosses threshold (e.g., btc:80000). Use multiple times for multiple alerts.")
args = parser.parse_args()

# Parse alerts into a {coingecko_id: threshold} dictionary
alerts = {}
if args.alert:
    for raw in args.alert:
        if ":" not in raw:
            print(f"⚠️  Bad alert format: '{raw}' (expected ticker:price, e.g., btc:80000)")
            continue
        ticker, threshold = raw.split(":", 1)
        ticker = ticker.lower()
        if ticker not in TICKERS:
            print(f"⚠️  Unknown ticker in alert: '{ticker}'")
            continue
        try:
            alerts[TICKERS[ticker]] = float(threshold)
        except ValueError:
            print(f"⚠️  Bad price in alert: '{threshold}'")
            
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

# Build the API URL
ids = ",".join(coin_ids)
url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"


def fetch_and_print():
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
    except requests.RequestException as e:
        print(f"⚠️  Network error: {e}")
        return

    if response.status_code != 200:
        print(f"⚠️  API error (status {response.status_code}). Try again in a moment.")
        return

    print()
    print(f"{'COIN':<12} {'PRICE (USD)':>15}")
    print("-" * 28)
    for coin in coin_ids:
        if coin in data and "usd" in data[coin]:
            price = data[coin]["usd"]
            marker = ""
            if coin in alerts and price >= alerts[coin]:
                marker = "  🚨 ALERT"
            print(f"{coin.capitalize():<12} ${price:>14,.2f}{marker}")
        else:
            print(f"{coin.capitalize():<12} {'(no data)':>15}")

    print()


if args.watch:
    try:
        while True:
            fetch_and_print()
            print(f"(refreshing every {args.watch}s — press Ctrl+C to stop)")
            time.sleep(args.watch)
    except KeyboardInterrupt:
        print("\nStopped. 👋")
else:
    fetch_and_print()