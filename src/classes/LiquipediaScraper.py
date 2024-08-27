import json
from classes.Scrape import Scrape
from classes.Chat import Chat
from bs4 import BeautifulSoup

liquipedia_url = "https://liquipedia.net"

class LiquipediaScraper(Scrape):
    def __init__(self, url=None):
        super().__init__(url=url, scrape_type=Scrape.Type.LOAD, load_time=3)

    def processOutput(self, soup):
        links = [link.get('href') for link in soup.find_all('a')]
        links_json = json.dumps(links)

        chat = Chat()
        question = (
            "Your response must strictly be that of an array that can be decoded by JSON "
            "(no extra characters as this needs to be read directly by a JSON decoder). "
            "This JSON must be a list of URLs (no extra properties), please return a list of all the relevant "
            "Rocket League tournament links of 2024. Exclude links to past years, to teams, or to players "
            "as we want only relevant tournament pages, RLCS or not. Here are the links to look through: "
            f"{links_json}"
        )
        print("Liquipedia: Scanning for tournament links...")
        chat_response = chat.ask(question)
        print(chat_response)

        tournaments = []
        page_chat = Chat()
        try:
            links = json.loads(chat_response)
            print("Liquipedia: Total links found: " + str(len(links)))
            print("Liquipedia: Scanning links for information...")
            for link in links:
                self.url = liquipedia_url + link
                page_soup = self.get_static()

                infobox = page_soup.find('div', class_='fo-nttax-infobox-wrapper infobox-rocket')
                if infobox is not None:
                    infobox_html = infobox.prettify()

                    question = (
                        "Please analyze the following snippet of HTML to extract key tournament information. "
                        'I am expecting a string that resembles this model {"tournament_name":"example","start_date":"YYYY-MM-DD","end_date":"YYYY-MM-DD","prize_pool": "100"}. Your response must NOT include a ```json prefix and must follow my strict guidelines. Currency must be an integer and foreign currencies can be roughly translated by you.'
                        "If information cannot be found, then leave the property null."
                        f"HTML SNIPPET: {infobox_html}"
                    )
                
                    page_chat_response = page_chat.ask(question)
                    print(page_chat_response)
                    tournament = json.loads(page_chat_response)
                
                    # Add the decoded tournament object to the tournaments array
                    tournaments.append(tournament)
                else:
                    print(f"No infobox found in {link}")

        except Exception as e:
                print(f"Error: {str(e)}")
                print(page_chat_response)
                print("JSON parse failed, trying again...")

                keep_trying = True
                while keep_trying:
                    try:
                        page_chat_response = page_chat.ask(
                            "Our parser failed to decode your response, please try again and remember the strict guidelines"
                        )
                        tournament = json.loads(page_chat_response)
                        tournaments.append(tournament)
                        break
                    except Exception as e:
                        print(f"Error {str(e)}")
                        print(page_chat_response)
                        print("JSON parse failed again, retrying...")
                        keep_trying = True
                print(page_chat_response)

        return tournaments
