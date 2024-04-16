class Locator:
    SEARCH_INPUT = "//*[@id='ybar-sbq']"
    SEARCH_BUTTON = "//*[@id='ybar-search']"
    
    CATEGORIES_BAR = "//*[@id='horizontal-bar']/ol/li[1]/div"
    MORE_BUTTON = "//*[@id='horizontal-bar']/ol/li[1]/div/div[3]/a"
    MORE_CATEGORIES = "//*[@id='horizontal-bar']/ol/li[1]/div/div[2]"
    NEWS_TAB = "//*[@id='horizontal-bar']/ol/li[1]/div/div[1]/ul/li[2]/a"
    VIDEOS_TAB = "//*[@id='horizontal-bar']/ol/li[1]/div/div[1]/ul/li[3]/a"
    IMAGES_TAB = "//*[@id='horizontal-bar']/ol/li[1]/div/div[1]/ul/li[4]/a"
    LOCAL_TAB = "//*[@id='horizontal-bar']/ol/li[1]/div/div[2]/ul/li[1]/a"
    SHOPPING_TAB = "//*[@id='horizontal-bar']/ol/li[1]/div/div[2]/ul/li[2]/a"
    
    NEWS = "//*[@id='web']//div[@class='dd NewsArticle']"
    NEWS_TITLE = "//*[@id='web']/ol/li[1]/div/ul/li/h4"
    NEWS_URL = ".//h4/a"
    NEWS_SOURCE = ".//span[@class='s-source']"
    NEWS_TIME = ".//span[@class='fc-2nd s-time']"
    NEWS_DESCRIPTION = ".//p[@class='s-desc']"
    
    # NEWS = "//*[@id='web']"
    # VIDEOS = "//*[@id='search']/div"
    # IMAGES = "//*[@id='results']"
    # LOCAL = "//*[@id='web']"
    # SHOPPING = "//*[@id='__next']/div[1]/div[2]/div/main/div/div[2]"
    