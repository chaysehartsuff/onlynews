from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from ScraperType import ScraperType
import requests
from enum import Enum

class Scrape:
    class Type(Enum):
        STATIC = 1
        LOAD = 2

    def __init__(self, url=None, scrape_type=Type.STATIC, load_time=0, base_url = ""):
        """Constructor to set the url property and type of scraping."""
        self.url = url
        self.scrape_type = scrape_type
        self.load_time = load_time
        self.base_url = base_url

    def get(self):
        """Determines which method to use based on the type and processes the output."""
        if not self.url:
            raise ValueError("URL is not set.")

        if self.scrape_type == Scrape.Type.STATIC:
            soup = self.get_static()
        elif self.scrape_type == Scrape.Type.LOAD:
            soup = self.get_load()
        else:
            raise ValueError("Invalid scrape type.")

        return self.processOutput(soup)

    def get_static(self):
        """Loads HTML from a page without using Selenium for static pages."""
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            raise Exception(f"Failed to retrieve page. Status code: {response.status_code}")

    def get_load(self):
        """Loads HTML using Selenium for dynamic pages, returns a BeautifulSoup object."""
        # Setup Selenium with Chrome
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode (no GUI)
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        
        with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver:
            driver.get(self.url)
            WebDriverWait(driver, self.load_time).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            rendered_html = driver.page_source
            soup = BeautifulSoup(rendered_html, 'html.parser')
            return soup
    def getType():
        return ScraperType.BASE

    def processOutput(self, soup):
        """Process the BeautifulSoup object and return the prettified HTML."""
        return soup.prettify()
