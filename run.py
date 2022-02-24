from premier_league.league import PremierLeague
from premier_league.report import PremierLeagueClub
import csv


def scrape():
    with PremierLeague() as bot:
        bot.implicitly_wait(3)
        bot.maximize_window()
        bot.league_homepage()
        bot.accept_cookies()
        bot.premier_table()
        bot.filter_by_competition("Premier League")
        bot.filter_by_season()
        bot.filter_by_home_or_away()
        bot.league_table()


def view_premier(team_name) -> list:
    store_obj = []

    with open("table_data\English Premier League.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
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
            store_obj.append(obj)
    for item in store_obj:
        if item.club == team_name:
            obj = item
    return obj
