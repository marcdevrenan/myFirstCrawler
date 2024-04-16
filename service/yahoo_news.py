from RPA.Browser.Selenium import Selenium
from config import BASE_URL, SEARCH_PHRASE, CATEGORY, PATH
from locators import Locator as LO
from service.crawler import Crawler
from service.helper import Helper

import logging


class YahooApi:
    def __init__(self) -> None:
        self.browser = Selenium()
        self.browser.open_chrome_browser
        self.browser.open_available_browser(url=BASE_URL)
        self.browser.maximize_browser_window()
    
    def process(self):
        self.browser.click_element_when_visible(LO.SEARCH_INPUT)
        self.browser.input_text(LO.SEARCH_INPUT, SEARCH_PHRASE)
        self.browser.click_button(LO.SEARCH_BUTTON)
        self.browser.switch_window(locator="NEW", timeout=2000)
        
        categories_element=self.browser.find_elements(LO.CATEGORIES_BAR)
        category_text=self.browser.get_text(categories_element)
        categories_list=category_text.split('\n')
        
        more=self.browser.find_element(LO.MORE_BUTTON)
        self.browser.click_element(more)
        more_categories_element=self.browser.find_element(LO.MORE_CATEGORIES)
        more_categories_text=self.browser.get_text(more_categories_element)
        more_categories_list=more_categories_text.split('\n')
        categories_list.extend(more_categories_list)
        
        categories_list = Helper.format_categories(categories_list)
        
        category_tab_locator = getattr(LO, f"{CATEGORY.upper()}_TAB")
        category_tab_element = self.browser.find_element(category_tab_locator)
        
        if category_tab_element:
            self.browser.click_element(category_tab_element)
            logging.info(f"Clicked on {CATEGORY} tab")
        else:
            logging.info(f"No tab found for category: {CATEGORY}")
        
        crawler = Crawler(self.browser)
        selected_method = getattr(crawler, f"extract_{CATEGORY.lower()}_data", None)
        if selected_method:
            data = selected_method()
            crawler.store_data_to_excel(data, PATH)
        else:
            logging.info(f"No method found for category: {CATEGORY}")
    
    def start(self):
        self.process()
