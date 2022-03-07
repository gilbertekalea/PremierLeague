# Author: Gilbert Ekale Amoding.

import csv
from prettytable import PrettyTable
import premier_league.constants as const

from selenium.common.exceptions import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class PastLeagueTable:
    """
    A class to scrape the premier league table
    param: WebDrive
    """
    def __init__(self, past_table: WebDriver):
        self.past_table = past_table

    def league_table_head(self) -> list:
        """
        Takes a web element as a parameters, and scrapes the premier league table headers.
        The method is quite slow and it's not used in any scraping activities.
        Instead we have hand written the premier league table headers; see method below.
        """
        # This method is not really necessary if you know the table heads; See the method below where we have
        # curated the list of table headers.
        abbreviated = ["More", "Pos", "Pl", "W", "D", "L", "Pts"]
        headers = []
        selected_table = self.past_table.find_element(By.TAG_NAME, "table")
        # Selects table by html tag name
        # based on the result above, select thead and the selects childrens.

        table_head = selected_table.find_element(By.TAG_NAME, "thead").find_elements(
            By.TAG_NAME, "th"
        )

        for head in table_head:
            elements_with_div = head.find_elements(By.TAG_NAME, "div")
            elements_with_abbr = head.find_elements(By.TAG_NAME, "abbr")

            if elements_with_div:
                for item in elements_with_div:

                    # ignore abbreaviated values such a pos, pl, w etc.
                    if (
                        item.get_attribute("innerHTML") in abbreviated
                        or item.get_attribute("innerHMTL") == "More"
                    ):
                        continue

                    else:
                        element = item.get_attribute("innerHTML")
                        headers.append(element)
            elif elements_with_abbr:
                for item in elements_with_abbr:
                    element = item.get_attribute("innerHTML")
                    headers.append(element)
            else:
                if head.get_attribute("innerHTML") in abbreviated:
                    element = head.get_attribute("innerHTML")
                    headers.append(element)

        return headers

    def league_table_body(self) -> tuple:
        """
        focus in the table body; perform different actions to collect the table data.
        """
        # premier league table data
        table_header = const.PREMIER_LEAGUE_TABLE_HEADERS
        pl_table = self.past_table.find_element(By.TAG_NAME, "table")

        body = pl_table.find_element(By.TAG_NAME, "tbody")
        rows = body.find_elements(By.CSS_SELECTOR, 'tr[data-filtered-entry-size="20"]')

        # Wrapper for printing table on the terminal
        data_pretty_table = []

        # Wraps rows td data
        td_data = []
        for row in rows:
            td = row.find_elements(By.TAG_NAME, "td")

            # We want to use hovering action ;for next_game header; This action will help us to collect
            # Extra information about the next_game; such time, dates, and competing teams.

            # # create action for hovering
            # hover = ActionChains(self.past_table)

            # # select element to perform hovering action'
            # try:
            #     obj = row.find_element(
            #         By.CSS_SELECTOR, 'td[class="nextMatchCol hideMed"]'
            #     )

            #     # perform the action
            #     hover.move_to_element(obj).perform()

            # except NoSuchElementException:
            #     pass
            # finally:
            #     pass

            td_D = {}
            club_form = []
            header_index = 0  # tracks index for table_header list.
            for data in td:
                if data.text == "":
                    continue

                if "\n" in data.text:
                    new_data = data.text.split("\n")
                    form = []
                    for i in new_data:
                        form.append(i)
                    club_form.append(form)
                    td_D[table_header[header_index]] = form
                    header_index += 1

                else:
                    # for pretty_table
                    club_form.append(data.text)

                    # for csv
                    td_D[table_header[header_index]] = data.text
                    header_index += 1

            td_data.append(td_D)
            data_pretty_table.append(club_form)
        return td_data, data_pretty_table

    @staticmethod
    def print_pretty_table(collections) -> None:
        """
        This function prints the premier league table on terminal using pretty tables module.
        """
        tab = PrettyTable()
        tab.field_names = const.PREMIER_LEAGUE_PAST_SEASON_TABLE_HEADERS
        tab.add_rows(collections)

        print(tab)
        
    @staticmethod
    def write_to_csv(dictionary) -> None:
        with open(
            f'table_data\{const.LEAGUES_URL[0]["league_name"]}.csv', "w", newline=""
        ) as csvfile:
            fieldnames = const.PREMIER_LEAGUE_PAST_SEASON_TABLE_HEADERS
            table_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            table_writer.writeheader()
            for index, row in enumerate(dictionary):
                table_writer.writerow(row)
