# Author: Gilbert Ekale Amoding

'''
This file contain methods and steps for scraping the premier league table. 
It provides foundation starting point for the bot. 
'''
import premier_league.constants as const
from premier_league.table import LeagueTable

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
        # temporary pop up  for ads if the premier leagues wants to advertised something for users to click.
        try:
            add_tab = self.find_element_by_id("advertClose")
            add_tab.click()
        except ElementNotInteractableException or NoSuchElementException:
            pass

    
    def premier_league_table(self)-> None:
        # On the homepage, click sub navigation bar 
        try:
            select_table_nav = self.find_element_by_css_selector(
                'li[data-nav-index="3"]'
            )
            select_table_nav.click()

        except NoSuchElementException:
            # if the table sub navigation is not found, start the url directly to the premier league table page.
            self.get("https://www.premierleague.com/tables")
                    
    def filter_by_competition(self, competition_name='Premier League'):

        '''
        This function filters the table by competition name: The focus of this scraping bot is on premier league:
        By default; the value is premier league.
        '''
        # find elemenet and click to initiate a drop down menu.
        dropdown_filter= self.find_element_by_css_selector(
                'div[data-dropdown-current="FOOTBALL_COMPETITION"]'
            )
        dropdown_filter.click()
            
        # find parent ul
        competition_list = self.find_element(By.CSS_SELECTOR, 'ul[data-dropdown-list="FOOTBALL_COMPETITION"]')

        # find children of ul element
        competition_type = competition_list.find_elements(By.CSS_SELECTOR, 'li[role="option"]')
        
        for comp_name in competition_type:
            if comp_name.get_attribute("innerHTML") == competition_name:
                comp_name.click()
                break
            else:
                continue

    def filter_by_season(self, season_name) -> None:
        season_dropdown_filter = self.find_element(By.CSS_SELECTOR, 'div[data-dropdown-current="compSeasons"]')
        season_dropdown_filter.click()
    
        seasons_list = self.find_element(By.CSS_SELECTOR, 'ul[data-dropdown-list="compSeasons"]')
        season_type = seasons_list.find_elements(By.CSS_SELECTOR, 'li[role="option"]')
        
        # loop through the list and find the element whose innerHTML content corresponde to season_name
        for season in season_type:
            if season.get_attribute('innerHTML') == season_name:
                season.click()
                break
            else:
                continue

    def filter_by_home_or_away(self, filter_criteria) -> None:
        ''''
        filter_critea => either `filter by away, home or all matches` default is all matches
        filter the table by game played at home or away.
        by default it's all_matches- i.e home and away are displayed.
        '''
        filter_home_away = self.find_element_by_css_selector(
            'div[data-dropdown-block="homeaway"]'
        )
        filter_home_away.click()
        
        select_ul_element = self.find_element_by_css_selector(
            'ul[data-dropdown-list="homeaway"]'
        )

        filters = select_ul_element.find_elements(By.CSS_SELECTOR, 'li[role="option"]')

        for item in filters:
            if item.get_attribute('innerHTML') == filter_criteria:
                item.click()
                break
            else:
                continue
    
    def close_live_button(self):
        '''
        improves the resistance of the bot when scrape is done during matchday weeks; where the premier league table is live;
        The bot closes the live button as to provide the regular table view. 
        '''
        try:
            live_button = self.find_element_by_css_selector('button[class="toggle-btn__toggle js-live-toggle"]')
            live_button.click()

        except NoSuchAttributeException or NoSuchElementException or ElementNotInteractableException:
            pass

    # All the preliminary steps are done. The bot is ready to focus on the table and scrape datae. 
    def league_table(self) -> None:
        table = LeagueTable(table=self)
        data = table.league_table_body()
        LeagueTable.write_to_csv(data[0])
        LeagueTable.print_pretty_table(data[1])
