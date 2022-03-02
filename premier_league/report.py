"""
This file contain methods that can be used to perform basic statistical analysis about the premier league teams. 

"""
from dataclasses import dataclass
import ast, csv, time
from prettytable import PrettyTable


@dataclass
class PremierLeagueTableHeader:
    position: str
    club: str
    played: int
    won: int
    drawn: int
    lost: int
    gf: int
    ga: int
    gd: int
    points: int
    form: list
    next_game: list


class PremierLeagueClub(PremierLeagueTableHeader):
    """ """

    def get_next_game(self) -> PrettyTable():
        """
        Returns PrettyTable object that contains details information about the clubs
        next game data.

        example:
        >>> obj = run.view_premier('Manchester United')
            obj.get_win_draw_lost_rate()
            +-------------------+-------------+-------------+-----------+--------------+
            |        Club       |    Action   | Wining rate | draw rate | Loosing rate |
            +-------------------+-------------+-------------+-----------+--------------+
            | Manchester United | Probability |     0.5     |    0.21   |     0.29     |
            +-------------------+-------------+-------------+-----------+--------------+
        """
        next_game_table = PrettyTable()
        # converting string list literal into normal list
        fixture = ast.literal_eval(self.next_game)

        next_game = [
            self.club,
            "vs",
        ]

        for index, item in enumerate(fixture):
            if index == 0 or index == 1 or index == 3:
                next_game.append(item)
            else:
                continue

        next_game_table.field_names = ["Current Team", " ", "Opponent", "date", "time"]
        next_game_table.add_row(next_game)
        return next_game_table

    def get_wdl_rate(self) -> PrettyTable():
        """
        calculates the win rate, draw rate  and loose rate of a team.
        calculations:
            win_rate = number_of_games_won/number_of_games_played
            draw_rate = number_of_games_drawn/number_of_games_played
            lose_rate = number_of_games_lost/ number_of_games_played
        example:
        >>> obj = run.view_premier('Manchester United')
            obj.get_wdl_rate()

            +-------------------+-------------+-------------+-----------+------------------+
            |        Club       |   Games Played  | Wining rate | draw rate | Loosing rate |
            +-------------------+-----------------+-------------+-----------+--------------+
            | Manchester United |         37      |     0.5     |    0.27   |     0.23     |
            +-------------------+-------------+-------------+-----------+------------------+
        """
        pretty_table = PrettyTable()

        wdl = [
            self.club,
            self.played,
            round(self.won / (self.played) * 1, 2),
            round(self.drawn / (self.played) * 1, 2),
            round(self.lost / (self.played) * 1, 2),
        ]
        pretty_table.field_names = [
            "Club",
            "Games Played",
            "Win rate",
            "draw rate",
            "Loose rate",
        ]

        pretty_table.add_row(wdl)
        return pretty_table

    def compare(self, other_team) -> tuple(PrettyTable()):
        """
        Compares two teams wdl rate and displays it in a tabular format
        """
        clubs = PremierLeagueClub.create_premier_clubs()
        other_table = PrettyTable()

        for obj in clubs:
            if obj.club == other_team:
                # construct a pretty table for the other_team wdl_rate table.
                wdl = [
                    obj.club,
                    obj.played,
                    round(obj.won / (obj.played) * 1, 2),
                    round(obj.drawn / (obj.played) * 1, 2),
                    round(obj.lost / (obj.played) * 1, 2),
                ]
                other_table.field_names = [
                    "Club",
                    "Games Played",
                    "Win rate",
                    "draw rate",
                    "Loose rate",
                ]
                other_table.add_row(wdl)
                
                # where pretty table magic happens
                print(
                    f"{self.club.upper()} WIN, DRAW & LOOSE RATE AFTER {self.played} GAMES"
                )
                time.sleep(5)
                print(self.get_wdl_rate())
                time.sleep(3)

                print(
                    f"{obj.club.upper()} WIN, DRAW & LOOSE RATE AFTER {obj.played} GAMES"
                )
                time.sleep(5)
                print(other_table)
            else:
                continue

        # return other_table

    @staticmethod
    def create_premier_clubs() -> list:
        """
        Functions reads through a csv file, instantiate `PremierLeagueClub` class.
        It's stores object created in a list.
        returns a list of objects.
        """
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
                store_obj.append(obj)
        return store_obj
