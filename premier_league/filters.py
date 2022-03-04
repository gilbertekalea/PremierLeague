import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class PremierLeagueTableFilter:

    def __init__(self, filters: WebDriver):
        self.filters= filters

    def filter_by_competition(self, competition_name="Premier League"):
        """
        This function filters the table by competition name: The focus of this scraping bot is on premier league:
        By default; the value is premier league.
        """
        # find elemenet and click to initiate a drop down menu.
        dropdown_filter = self.filters.find_element_by_css_selector(
            'div[data-dropdown-current="FOOTBALL_COMPETITION"]'
        )
        dropdown_filter.click()

        # find parent ul
        competition_list = self.filters.find_element(
            By.CSS_SELECTOR, 'ul[data-dropdown-list="FOOTBALL_COMPETITION"]'
        )

        # find children of ul element
        competition_type = competition_list.find_elements(
            By.CSS_SELECTOR, 'li[role="option"]'
        )

        for comp_name in competition_type:
            if comp_name.get_attribute("innerHTML") == competition_name:
                comp_name.click()
                break
            else:
                continue

    def filter_by_season(self, season_name) -> None:
        season_dropdown_filter = self.filters.find_element(
            By.CSS_SELECTOR, 'div[data-dropdown-current="compSeasons"]'
        )
        season_dropdown_filter.click()

        seasons_list = self.filters.find_element(
            By.CSS_SELECTOR, 'ul[data-dropdown-list="compSeasons"]'
        )
        season_type = seasons_list.find_elements(By.CSS_SELECTOR, 'li[role="option"]')

        # loop through the list and find the element whose innerHTML content corresponde to season_name
        for season in season_type:
            if season.get_attribute("innerHTML") == season_name:
                season.click()
                break
            else:
                continue

    def filter_by_home_or_away(self, filter_criteria) -> None:
        """'
        filter_critea => either `filter by away, home or all matches` default is all matches
        filter the table by game played at home or away.
        by default it's all_matches- i.e home and away are displayed.
        """
        filter_home_away = self.filters.find_element_by_css_selector(
            'div[data-dropdown-block="homeaway"]'
        )
        filter_home_away.click()

        select_ul_element = self.filters.find_element_by_css_selector(
            'ul[data-dropdown-list="homeaway"]'
        )

        filters = select_ul_element.find_elements(By.CSS_SELECTOR, 'li[role="option"]')

        for item in filters:
            if item.get_attribute("innerHTML") == filter_criteria:
                item.click()
                break
            else:
                continue

        time.sleep(5)

    def close_live_button(self):
        """
        improves the resistance of the bot when scrape is done during matchday weeks; where the premier league table is live;
        The bot closes the live button as to provide the regular table view.
        """
        try:
            live_button = self.filters.find_element_by_css_selector(
                'button[class="toggle-btn__toggle js-live-toggle"]'
            )
            live_button.click()
        except ElementNotInteractableException:
            pass
