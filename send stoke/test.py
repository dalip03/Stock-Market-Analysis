from yahoo_fin.stock_info import *
import yahoo_fin.stock_info as si


def tabledata():
    # Stocklist = ['TSLA','AAPL','BAC','MARA','AMZN','NVDA','NIO','RIOT','GOOGL','INFY','PLUG','APE','SOFI','META','MSFT','SNAP','USB','NYCB','DNA','UBER','AFRM','PYPL','PARA','MS','DELL','HPQ','HPE','DIS']
    Stocklist = ['TSLA','AAPL','BAC']
    # temp = si.get_quote_data('TSLA')
    # stock_data = []
    for i in Stocklist:
        
        temp = (si.get_quote_data(i))
        print(temp)

tabledata()