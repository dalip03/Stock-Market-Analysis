

from yahoo_fin.stock_info import *
import yahoo_fin.stock_info as si
# from yahoo_fin import options
import pandas as pd

def tabledata():
    Stocklist = ['TSLA','AAPL','BAC','MARA','AMZN','NVDA','NIO','RIOT','GOOGL','INFY','PLUG','APE','SOFI','META','MSFT','SNAP','USB','NYCB','DNA','UBER','AFRM','PYPL','PARA','MS','DELL','HPQ','HPE','DIS']
    # Stocklist = ['TSLA','AAPL','BAC']
    # temp = si.get_quote_data('TSLA')
    stock_data = []
    for i in Stocklist:
        
        temp = (si.get_quote_data(i))
        # temp[i] = (si.get_data(i, start_date = '24/04/2023'))
        stock_data.append([temp['symbol'],
            temp['regularMarketPrice'],
            temp['regularMarketDayHigh'],
            temp['regularMarketDayLow'],
            temp['marketCap'],
            temp['regularMarketVolume'],
            temp['regularMarketDayRange'],
            temp['regularMarketPreviousClose'],
            temp['averageDailyVolume3Month'],
            temp['averageDailyVolume10Day'],
            temp['fiftyTwoWeekLowChange'],
            temp['fiftyTwoWeekRange'],
            temp['fiftyTwoWeekHigh'],
            temp['fiftyTwoWeekLow']])

    columns_table = ['Stock Code',
                   'R.M Price',
                   'R.M Day High',
                   'R.M Day Low',
                   'Market Cap',
                   'R.M Volume',
                   'R.M Day Range',
                   'R.M Prev. Close',
                   'Avg.Daily volume 3Month',
                   'Avg.Daily volume 10Day',
                   '52 Week Low Change',
                    '52 Week Range',
                    '52 Week High',
                    '52 Week Low']    
    return(stock_data, columns_table)
#     print( stock_data[0:2] , columns_table)
# tabledata()