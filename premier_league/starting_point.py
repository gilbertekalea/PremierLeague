# Author: Gilbert Ekale Amoding
"""
This file contain methods and steps for scraping the premier league table. 
It provides foundation starting point for the bot. 
"""

import premier_league.constants as const
from premier_league.current_season_crawler import CurrentLeagueTable
from premier_league.past_seasons_crawler import PastLeagueTable
from premier_league.filters import PremierLeagueTableFilter
import os
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BotStartingPoint(webdriver.Chrome):
    def __init__(
        self, driver_path=r"C:\Users\gilbe\Desktop\SeleniumDrivers", teardown=True
    ):
        self.driver_path = driver_path
        self.teardown = teardown

        # system level >>>>> operating system path to environment variables.
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument('--headless')
        # Used to instantiate the webdriver.chrome class so that the Booking will inherit all the methods.
        super(BotStartingPoint, self).__init__(options=options)
        # gives the child a full access to parent class methods.

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        if self.teardown:
            self.quit()

    def premier_league_homepage(self) -> None:
        # league home_page
        self.get(const.LEAGUES_URL[0]["website"])

    def accept_cookies(self) -> None:
        # handles cookies modal window. acccepts all cookies
        try:
            # if the cookies element exits and can be accessed.
            cookies = self.find_element_by_css_selector(
                'button[class="_2hTJ5th4dIYlveipSEMYHH BfdVlAo_cgSVjDUegen0F js-accept-all-close"]'
            )
            cookies.click()

        except NoSuchElementException or ElementNotVisibleException or ElementNotInteractableException:
            print("No cookies available")

    def close_ads(self) -> None:
        '''
        Sometimes the website displays ads for voting or promoting events. this function looks up for this element ; if it's available 
        it closes. 
        '''
        try:
            add_tab = self.find_element_by_id("advertClose")
            add_tab.click()
        except ElementNotInteractableException or NoSuchElementException:
            pass

    def premier_league_table(self) -> None:
        # On the homepage, click sub navigation bar
        try:
            select_table_nav = self.find_element_by_css_selector(
                'li[data-nav-index="3"]'
            )
            select_table_nav.click()

        except NoSuchElementException:
            # if the table sub navigation is not found, start the url directly to the premier league table page.
            self.get("https://www.premierleague.com/tables")
            

    # All the preliminary steps are done. The bot is ready to focus on the table and scrape datae.
    def league_table(self) -> None:
        '''
        Prompt users to enter which season they want to scrape data from. 
        The table for current season and past seasons are quite different. 
        '''
        filtration = PremierLeagueTableFilter(filters=self)
        season = input('Current Season or Past? C | P : ')
        if season == 'C' or season == 'c':
            filtration.filter_by_competition()
            filtration.filter_by_season('2021/22')
            filtration.filter_by_home_or_away(input("Enter Home | Away | All Matches: "))
            filtration.close_live_button()
            table = CurrentLeagueTable(table=self)
            data = table.league_table_body()
            CurrentLeagueTable.write_to_csv(data[0])
            CurrentLeagueTable.print_pretty_table(data[1])

        elif season == 'P' or season == 'p':
            filtration.filter_by_competition()
            filtration.filter_by_season(input('Enter the season: Please follow premier league format 2020/21: '))
            filtration.filter_by_home_or_away(input("Enter Home | Away | All Matches: "))
            table = PastLeagueTable(past_table=self)
            data = table.league_table_body()
            PastLeagueTable.write_to_csv(data[0])
            PastLeagueTable.print_pretty_table(data[1])

