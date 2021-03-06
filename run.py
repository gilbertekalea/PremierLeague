from unicodedata import name
from premier_league.starting_point import BotStartingPoint
from premier_league.filters import PremierLeagueTableFilter
from premier_league.current_report import PremierLeagueClub
import time


def start_scraping():
    print('waking up the bot!!')
    with BotStartingPoint() as bot:
        print('Hello, there! Thank you for waking me up. It might take a while;\n Working to prepare for the adventure')
        bot.implicitly_wait(15)
        bot.maximize_window()
        bot.premier_league_homepage()
        bot.accept_cookies()
        bot.premier_league_table()
        time.sleep(5)
        bot.league_table()

def view_premier(club_name) -> list:
    clubs = PremierLeagueClub.create_premier_clubs()
    for item in clubs:
        if item.club == club_name:
            obj = item
    return obj
