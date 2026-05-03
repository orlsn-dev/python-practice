import string
import argparse

parser = argparse.ArgumentParser(description="Generate a secure random password.")
parser.add_argument("--length", type=int, default=16, help="Password length (default: 16)")
parser.add_argument("--symbols", action="store_true", help="Include symbols")
parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
parser.add_argument("--count", type=int, default=1, help="How many passwords to generate")

args = parser.parse_args()

characters = string.ascii_letters
if not args.no_digits:
    characters += string.digits
if args.symbols:
    characters += string.punctuation

for _ in range(args.count):
    password = "".join(random.choice(characters) for _ in range(args.length))
    print(password)