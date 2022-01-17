from prettytable import PrettyTable
from selenium.common.exceptions import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LeagueTable:
    def __init__(self, tables: WebDriver):
        self.tables = tables

    def select_table_head(self):
        # This method is not really necessary if you know the table heads; See the method below where we have 
        # curated the list of table headers. 
        abbreviated = ['More', 'Pos', 'Pl', 'W', 'D', 'L', 'Pts']
        headers = []
        selected_table = self.tables.find_element(
            By.TAG_NAME, 'table')  # Selects table by html tag name
        # based on the result above, select thead and the selects childrens.

        table_head = selected_table.find_element(
            By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')

        for head in table_head:
            elements_with_div = head.find_elements(By.TAG_NAME, 'div')
            elements_with_abbr = head.find_elements(By.TAG_NAME, 'abbr')

            if elements_with_div:
                for item in elements_with_div:
                    # print(item.get_attribute('innerHTML'))
                    if item.get_attribute('innerHTML') in abbreviated or item.get_attribute('innerHMTL') == 'More':
                        continue
                    
                    else:
                        element = item.get_attribute('innerHTML')
                        headers.append(element)
            elif elements_with_abbr:
                for item in elements_with_abbr:
                    element = item.get_attribute('innerHTML')
                    headers.append(element)
            else:
                if head.get_attribute('innerHTML') in abbreviated:
                    element = head.get_attribute('innerHTML')
                    headers.append(element)
                    
        return headers

    def select_table_body(self):
        header = ['Position', 'Club', 'Played', 'Won', 'Drawn', 'Lost', 'GF','GA','GD', 'Points', 'Form','Next Game']

        body = self.tables.find_element(
            By.CSS_SELECTOR, 'tbody[class="tableBodyContainer isPL"]')
        rows = body.find_elements(
            By.CSS_SELECTOR, 'tr[data-filtered-entry-size="20"]')
        
        collection_list =[]
        td_dict = []
        for row in rows:
            td = row.find_elements(By.TAG_NAME, 'td')
            td_D = {}
            collection =[]
            header_index = 0
            for data in td:
                if data.text == '':
                    continue
                elif '\n' in data.text:
                    new_data = data.text.split('\n')
                    form = []
                    for i in new_data:
                        form.append(i)
                    collection.append(form)
                    
                    td_D[header[header_index]] = form
                    header_index+=1
                else:
                    collection.append(data.text)    
                    td_D[header[header_index]] = data.text 
                    header_index+=1   
            td_dict.append(td_D)
            collection_list.append(collection)
        return td_dict, collection_list
        
    @staticmethod
    def print_pretty_table(collections):
        tab = PrettyTable()
        tab.field_names = ['Position', 'Club', 'Played', 'Won', 'Drawn',
                                'Lost', 'GF', 'GA', 'GD', 'Points', 'Form', 'Next Game']
        tab.add_rows(collections)
        print(tab)
        # Todos ---> DONE!!!
        #! Optimize the code by storing data in dictionary format.
        # Create a dictionary for table values and headers
        # Save data on csv
        # Scrape more than one league, eg laliga, lique, and
