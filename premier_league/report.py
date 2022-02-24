from dataclasses import dataclass

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
        return f"${self.club} will be playing against ${self.next_game}"

    def get_win_draw_lost_rate(self):
        return [
            "win:",
            (self.won / (self.played)) * 100,
            "Drawn:",
            self.drawn / (self.played) * 100,
            "Lost:",
            self.lost / (self.played) * 100,
        ]
