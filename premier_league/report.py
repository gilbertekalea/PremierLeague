from dataclasses import dataclass
from dis import pretty_flags


from prettytable import PrettyTable

@dataclass
class PremierLeagueClub:
    position: int
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
    next_game: str

    def get_next_game(self):
        return f'{self.club} will be playing against {self.next_game}'

    def get_win_draw_lost_rate(self)-> PrettyTable:
        '''
        it's calculates the winning,losing and drawing rate based on number of games played;
        Calculations:
            win_rate = number_of_games_won/number_of_games_played
            draw_rate = number_of_games_drawn/number_of_ganes_played
        
        >>> obj.get_win_draw_lost_rate()
            +-------------------+-------------+-------------+-----------+--------------+
            |        Club       |    Action   | Wining rate | draw rate | Loosing rate |
            +-------------------+-------------+-------------+-----------+--------------+
            | Manchester United | Probability |     0.5     |    0.27   |     0.23     |
            +-------------------+-------------+-------------+-----------+--------------+
        '''
        pretty_table = PrettyTable()

        statistic = [
            self.club, 
            'Probability', 
            round(self.won / (self.played)* 1,2), 
            round(self.drawn / (self.played)* 1, 2), 
            round(self.lost / (self.played) * 1, 2) 
            ]
        pretty_table.field_names= [
            'Club',
            'Action',
            'Wining rate',
            'draw rate', 
            'Loosing rate',
        ]
        
        pretty_table.add_row(statistic)
        return pretty_table
    