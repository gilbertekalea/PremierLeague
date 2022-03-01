from dataclasses import dataclass
import ast
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
    '''
    '''
    def get_next_game(self):
        next_game_table = PrettyTable()
        # converting string list literal into normal list
        fixture = ast.literal_eval(self.next_game)

        next_game= [self.club, 'vs', ]

        for index, item in enumerate(fixture):
            if index == 0 or index == 1 or index == 3:
                next_game.append(item)
            else:
                continue

        next_game_table.field_names = ["Current Team", " ", "Opponent", 'date', 'time']
        next_game_table.add_row(next_game)
        return next_game_table

    def get_win_draw_lost_rate(self) -> PrettyTable():

        """
        its calculates the winning,losing and drawing rate based on number of games played;
        Calculations:
            win_rate = number_of_games_won/number_of_games_played
            draw_rate = number_of_games_drawn/number_of_ganes_played

        >>> obj.get_win_draw_lost_rate()
            +-------------------+-------------+-------------+-----------+--------------+
            |        Club       |    Action   | Wining rate | draw rate | Loosing rate |
            +-------------------+-------------+-------------+-----------+--------------+
            | Manchester United | Probability |     0.5     |    0.27   |     0.23     |
            +-------------------+-------------+-------------+-----------+--------------+
        """
        pretty_table = PrettyTable()

        statistic = [
            self.club,
            "Probability",
            round(self.won / (self.played) * 1, 2),
            round(self.drawn / (self.played) * 1, 2),
            round(self.lost / (self.played) * 1, 2),
        ]
        pretty_table.field_names = [
            "Club",
            "Action",
            "Wining rate",
            "draw rate",
            "Loosing rate",
        ]

        pretty_table.add_row(statistic)
        return pretty_table
