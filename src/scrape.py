import sys
sys.path.append('/usr/src/app/classes')

import json
import os
import uuid
from config import config
from classes.ScraperType import ScraperType
from classes.LiquipediaScraper import LiquipediaScraper

# paths
dump_path = './dump'
os.makedirs(os.path.dirname(dump_path), exist_ok=True)

scrape_list = [
    LiquipediaScraper("https://liquipedia.net/rocketleague/S-Tier_Tournaments")  # Liquipedia S-Tier
]

# Run all Scrapers
tournaments = []
for scraper in scrape_list:
    if scraper.getType().value == ScraperType.TOURNAMENT.value:
        tournaments.extend(scraper.get())

#tournament dump
tournaments_path = config[ScraperType.TOURNAMENT.value]["dump_path"] + f"{uuid.uuid4().hex}.json"
with open(tournaments_path, 'w') as file:
    json.dump(tournaments, file, indent=4)
print(f"Tournaments saved to {tournaments_path}")


# DONE
print("scaper: Done scanning.")
