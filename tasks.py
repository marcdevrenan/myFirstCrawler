from service.yahoo_news import YahooApi

def runYahooNews():
    YahooApi().start()

if __name__=="__main__":
    runYahooNews()
