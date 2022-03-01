from unicodedata import name
from premier_league.starting_point import BotStartingPoint
from premier_league.report import PremierLeagueClub
import csv,time


def scrape():
    with BotStartingPoint() as bot:
        bot.implicitly_wait(5)
        bot.maximize_window()
        bot.premier_league_homepage()
        bot.accept_cookies()
        bot.premier_league_table()
        bot.filter_by_competition()
        bot.filter_by_season(input('Enter Season: '))
        bot.filter_by_home_or_away(input('Enter Home | Away | All Matches: '))
        
        bot.close_live_button()
        time.sleep(5)
        bot.league_table()

def view_premier(club_name) -> list:
    store_obj = []
    # read the csv
    with open("table_data\English Premier League.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # create instance for each team.
            obj = PremierLeagueClub(
                position=int(row["Position"]),
                club=row["Club"],
                played=int(row["Played"]),
                won=int(row["Won"]),
                drawn=int(row["Drawn"]),
                lost=int(row["Lost"]),
                gf=int(row["GF"]),
                ga=int(row["GA"]),
                gd=int(row["GD"]),
                points=int(row["Points"]),
                form=row["Form"],
                next_game=row["Next Game"],
            )
            # store each team in a list
            store_obj.append(obj)
    # loop through list of objects and return an obj where the club equals club_name
    for item in store_obj:
        if item.club == club_name:
            obj = item
    return obj
