from unicodedata import name
from premier_league.starting_point import BotStartingPoint
from premier_league.filters import PremierLeagueTableFilter
from premier_league.current_report import PremierLeagueClub
import time

def scrape():
    with BotStartingPoint() as bot:
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
