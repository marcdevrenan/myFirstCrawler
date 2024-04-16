from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
from locators import Locator as LO

import logging


class Crawler:
    def __init__(self, browser):
        self.browser = browser
    
    def extract_news_data(self):
        news_elements = self.browser.find_elements(LO.NEWS)
        
        news_data = []
        for element in news_elements:
            try:
                news_dict = {}
                news_dict['title'] = element.find_element(LO.NEWS_TITLE).text
                news_dict['url'] = element.find_element(LO.NEWS_URL).get_attribute("href")
                news_dict['source'] = element.find_element(LO.NEWS_SOURCE).text
                news_dict['time'] = element.find_element(LO.NEWS_TIME).text
                news_dict['description'] = element.find_element(LO.NEWS_DESCRIPTION).text
                news_data.append(news_dict)
            except Exception as e:
                logging.exception(f"Error extracting news data: {e}")
            
        return news_data
    
    def extract_videos_data(self):
        logging.info("Extracting videos data...")
    
    def extract_images_data(self):
        logging.info("Extracting images data...")
        
    def extract_local_data(self):
        logging.info("Extracting local data...")
        
    def extract_shopping_data(self):
        logging.info("Extracting shopping data...")
        
    def store_data_to_excel(self, data, path):
        excel = Files()
        excel.create_workbook(path)
        excel.add_worksheet("News")
        
        headers = ['Title', 'URL', 'Source', 'Time', 'Description']
        excel.append_rows_to_worksheet("News", headers)
        
        for news in data:
            row_data = [news['title'], news['url'], news['source'], news['time'], news['description']]
            excel.append_rows_to_worksheet("News", row_data)
            
        excel.save_workbook(path)
