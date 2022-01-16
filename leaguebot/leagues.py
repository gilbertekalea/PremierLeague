import leaguebot.constants as const
from leaguebot.table import LeagueTable
import os,time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

# This file contains method we will use to craw through the top leagues tables.


class SoccerLeagues(webdriver.Chrome):

    def __init__(self,  driver_path=r"C:\Users\gilbe\Desktop\workstation\projects\scrape\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        # self.implicitly_wait(20)
        # self.maximize_window()

        # system level >>>>> operating system path to environment variables.
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Used to instantiate the webdriver.chrome class so that the Booking will inherit all the methods.
        super(SoccerLeagues, self).__init__(options=options)
        # gives the child a full access to parent class methods.

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.teardown:
            self.quit()

    def league_homepage(self):
        # visit a homepage
        self.get(const.PREMIER_LEAGUE_URL)

    def accept_cookies(self):

        # handles cookies modal window. acccepts all cookies
        try:
            # if the cookies element exits and can be accessed.
            cookies = self.find_element_by_css_selector(
                'button[class="_2hTJ5th4dIYlveipSEMYHH BfdVlAo_cgSVjDUegen0F js-accept-all-close"]'
            )
            cookies.click()

        except NoSuchElementException or ElementNotVisibleException or ElementNotInteractableException:
            print('No such element.. ')

    def close_ads(self):
        # temporary pop up  for ads if the premier leagues wants to advertised something for users to click.

        try:
            add_tab = self.find_element_by_id("advertClose")
            add_tab.click()
            print('Add button closed')

        except ElementNotInteractableException or NoSuchElementException:
            print('No ads dictated')

    # on the homepage, click on subnavigation bar contain tables.
    def premier_table(self):
        try:
            select_table_nav = self.find_element_by_css_selector(
                'li[data-nav-index="3"]'
            )
            select_table_nav.click()
            # just incase we encouter ads again after loading premier league page.
            # self.close_ads()
        except NoSuchElementException:
            self.get('https://www.premierleague.com/tables')

    def filter_by_competition(self, competition_name):
        # filter by competition eg Premier League, FA Cup, UEFA Champions League
        try:
            competition_filter = self.find_element_by_css_selector(
            'div[data-dropdown-block="FOOTBALL_COMPETITION"]')

            competition_filter.click()
        except NoSuchElementException:
            competition_filter = self.find_element_by_css_selector(
                'div[aria-labelledby="dd-FOOTBALL_COMPETITION"]'
            )
        # # returns a list of `li` elements where role == options in
        competition = self.find_elements(By.CSS_SELECTOR,
                                         'li[role="option"]'
                                         )
        for comp_name in competition:
            if comp_name.get_attribute('innerHTML') == competition_name:
                comp_name.click()
                break
            else:
                continue

    def filter_by_season(self, season_name=None):
        # premier league seasons are in the following formats ==> 2012/13, 2013/14, 2020/21, 2021/22 [--> 2021 -2022]
        # By default the bot will select the present seasons --> Manually fixed. 
        
        # first click the competition dropdown menu for seasons
        div_season_filter = self.find_element_by_css_selector(
            'div[data-dropdown-block="compSeasons"]'
        )
        div_season_filter.click()

        # Then select ul element holding li elements containing seasons.
        ul_seasons = self.find_element_by_css_selector(
            'ul[data-dropdown-list="compSeasons"]')

        # Now, find all elements in ul_seasons. returns a list
        seasons = ul_seasons.find_elements(By.CSS_SELECTOR,
                                           'li[role="option"]'
                                           )

        # loop through the list and find the element whose innerHTML content corresponde to season_name
        for season in seasons:
            if season_name == None:
                season_name == '2021/22'
            if season.get_attribute('innerHTML') == season_name:
                season.click()
                # if the condition is met break out of the loop.
                break
            else:
                continue

    def filter_by_home_or_away(self, filter_criteria=None):
        # filter_critea => either `filter by away, home or all matches` default is all matches
        # filter the table by game played at home or away.
        # by default it's all_matches- i.e home and away are displayed.
        filter_home_away = self.find_element_by_css_selector(
            'div[data-dropdown-block="homeaway"]'
        )

        filter_home_away.click()

        select_ul_element = self.find_element_by_css_selector(
            'ul[data-dropdown-list="homeaway"]'
        )
        filters = select_ul_element.find_elements(
            By.CSS_SELECTOR, 'li[role="option"]')

        for filter in filters:
            if filter_criteria == None:
                filter_criteria = "All Matches"
                
            if filter.get_attribute('innerHTML') == filter_criteria:
                filter.click()
                break
            else:
                continue
            
    def league_table(self):
        table = LeagueTable(tables=self)
        # table.select_table_head()
        table.select_table_body()
        
        