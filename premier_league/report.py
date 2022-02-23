from dataclasses import dataclass


@dataclass
class PremierLeagueClub:
    
    position:int
    club: str
    played:int
    won:int
    drawn:int
    lost:int
    gf:int
    ga:int
    gd:int
    points:int
    form:list
    next_game:str
    
    def current_position(self, team_name):
        return self.position
    