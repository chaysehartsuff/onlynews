import json
import os
import uuid
from classes.Scrape import Scrape
from classes.LiquipediaScraper import LiquipediaScraper

random_filename = f"{uuid.uuid4().hex}.json"
dump_path = os.path.join('./dump', random_filename)
os.makedirs(os.path.dirname(dump_path), exist_ok=True)

scrape_list = [
    LiquipediaScraper("https://liquipedia.net/rocketleague/S-Tier_Tournaments")  # Liquipedia S-Tier
]

tournaments = []
for scraper in scrape_list:
    tournaments.extend(scraper.get())

with open(dump_path, 'w') as file:
    json.dump(tournaments, file, indent=4)

print(f"Tournaments saved to {dump_path}")

print("scaper: Done scanning.")
