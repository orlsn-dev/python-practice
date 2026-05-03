import requests
from bs4 import BeautifulSoup
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description="Scrape the Hacker News front page.")
parser.add_argument("--top", type=int, default=30, help="How many stories to show (max 30)")
0 8 * * * /Users/orlsn/python-practice/venv/bin/python /Users/orlsn/python-practice/hn.py --top 15 --min-score 100 --save >> /Users/orlsn/python-practice/cron.log 2>&1
parser.add_argument("--min-score", type=int, default=0, help="Only show stories with at least this many points")
parser.add_argument("--save", action="store_true", help="Save results to hn_briefing.txt")

args = parser.parse_args()

url = "https://news.ycombinator.com"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

stories = soup.find_all("tr", class_="athing")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

results = []

for story in stories:
    title_tag = story.find("span", class_="titleline").find("a")
    title = title_tag.get_text()
    link = title_tag["href"]

    subtext = story.find_next_sibling("tr")
    score_tag = subtext.find("span", class_="score")
    score_text = score_tag.get_text() if score_tag else "0 points"
    score_number = int(score_text.split()[0]) if score_tag else 0

    author_tag = subtext.find("a", class_="hnuser")
    author = author_tag.get_text() if author_tag else "unknown"

    if score_number >= args.min_score:
        results.append({
            "title": title,
            "link": link,
            "score": score_text,
            "score_number": score_number,
            "author": author,
        })

results = results[:args.top]

print(f"\nHacker News — {timestamp}")
print("=" * 50)
print(f"Showing {len(results)} stories (min score: {args.min_score})\n")

for i, story in enumerate(results, start=1):
    print(f"{i}. {story['title']}")
    print(f"   {story['score']} | by {story['author']}")
    print(f"   {story['link']}\n")

if args.save:
    with open("hn_briefing.txt", "w") as f:
        f.write(f"Hacker News Briefing — {timestamp}\n")
        f.write("=" * 50 + "\n\n")
        for i, story in enumerate(results, start=1):
            f.write(f"{i}. {story['title']}\n")
            f.write(f"   {story['score']} | by {story['author']}\n")
            f.write(f"   {story['link']}\n\n")
    print(f"Saved {len(results)} stories to hn_briefing.txt")