from leaguebot.leagues import SoccerLeagues

with SoccerLeagues() as leaguebot:
    leaguebot.implicitly_wait(3)
    leaguebot.maximize_window()
    leaguebot.league_homepage()
    leaguebot.accept_cookies()
    # leaguebot.close_ads()
    leaguebot.premier_table()
    leaguebot.filter_by_competition('Premier League')
    leaguebot.filter_by_season()
    leaguebot.filter_by_home_or_away()
    leaguebot.league_table()
    

    
    
    
        
