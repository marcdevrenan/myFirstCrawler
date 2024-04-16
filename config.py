from dotenv import load_dotenv
import os


load_dotenv(".env")
BASE_URL = "https://news.yahoo.com/"
SEARCH_PHRASE = os.environ.get("SEARCH_PHRASE")
CATEGORY = os.environ.get("CATEGORY")
PATH = "temp/news_data.xlsx"