# table-2 -->   <div class="D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)" data-test="right-summary-table"><table class="W(100%) M(0) Bdcl(c)"><tbody><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Market Cap</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="MARKET_CAP-value">2.619T</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Beta (5Y Monthly)</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="BETA_5Y-value">1.30</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>PE Ratio (TTM)</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="PE_RATIO-value">28.11</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>EPS (TTM)</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="EPS_RATIO-value">5.89</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Earnings Date</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="EARNINGS_DATE-value"><span>Apr 26, 2023</span> - <span>May 01, 2023</span></td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Forward Dividend &amp; Yield</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="DIVIDEND_AND_YIELD-value">0.92 (0.57%)</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Ex-Dividend Date</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="EX_DIVIDEND_DATE-value"><span>Feb 10, 2023</span></td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) Bdbw(0)! "><td class="C($primaryColor) W(51%)"><span>1y Target Est</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="ONE_YEAR_TARGET_PRICE-value">170.39</td></tr></tbody></table></div>
# Table - 1 -->  <div class="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)" data-test="left-summary-table"><table class="W(100%)"><tbody><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Previous Close</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="PREV_CLOSE-value">214.00</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Open</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="OPEN-value">215.73</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Bid</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="BID-value">219.90 x 1400</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Ask</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="ASK-value">220.05 x 3000</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Day's Range</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="DAYS_RANGE-value">215.82 - 221.15</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>52 Week Range</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="FIFTY_TWO_WK_RANGE-value">88.09 - 224.30</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Volume</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="TD_VOLUME-value"><fin-streamer data-symbol="META" data-field="regularMarketVolume" data-trend="none" data-pricehint="2" data-dfield="longFmt" value="23,253,821" active="">23,253,821</fin-streamer></td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) Bdbw(0)! "><td class="C($primaryColor) W(51%)"><span>Avg. Volume</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="AVERAGE_VOLUME_3MONTH-value">31,403,524</td></tr></tbody></table></div>
import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import os
import numpy as np
# price and change --> <div class="D(ib) Mend(20px)"><fin-streamer class="Fw(b) Fz(36px) Mb(-4px) D(ib)" data-symbol="AAPL" data-test="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehint="2" value="160.1" active="">160.10</fin-streamer><fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="AAPL" data-test="qsp-price-change" data-field="regularMarketChange" data-trend="txt" data-pricehint="2" value="-0.69999695" active=""><span class="C($negativeColor)">-0.70</span></fin-streamer> <fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="AAPL" data-field="regularMarketChangePercent" data-trend="txt" data-pricehint="2" data-template="({fmt})" value="-0.004353215" active=""><span class="C($negativeColor)">(-0.44%)</span></fin-streamer><fin-streamer class="D(n)" data-symbol="AAPL" changeev="regularTimeChange" data-field="regularMarketTime" data-trend="none" value="" active="true"></fin-streamer><fin-streamer class="D(n)" data-symbol="AAPL" changeev="marketState" data-field="marketState" data-trend="none" value="" active="true"><span class="e3b14781">PRE</span></fin-streamer><div id="quote-market-notice" class="C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)"><span>At close:  04:00PM EDT</span></div></div>


def stock_table_data():
    # Stocklist = ['TSLA','AAPL','BAC','MARA','AMZN','NVDA','NIO','RIOT','GOOGL','INFY','PLUG','APE','SOFI','META','MSFT','SNAP','USB','NYCB','DNA','UBER','AFRM','PYPL','PARA','MS','DELL','HPQ','HPE','DIS']
    Stocklist = ['TSLA','AAPL','BAC']
    
    
    DataMatrix = [[]]
    for StockCode in Stocklist:
        # print(StockCode)
       
        temp= []

        def web_table1(web_content, class_path, value):
            web_table = web_content.find_all('div', {'class': class_path})
            try:
                if value == 'None1':
                    texts1 = web_table[0].get_text("|", strip=True)
                    texts1 = texts1.split("|")
                    print(texts1)
        # ---> here text_temp = [Previous, Open ,Day's Range, 52 Week Range ,Volume, Avg. Volume ]
                    text_temp = [texts1[1], texts1[3], texts1[9],
                                texts1[11], texts1[13], texts1[15]]
                    texts1 = text_temp
                else:
                    texts1 = []
            except IndexError:
                texts1 = []

            return texts1

        def web_table(web_content, class_path, value):
            web_table = web_content.find_all('div', {'class': class_path})
            try:
                if value == 'None':
                    texts2 = web_table[0].get_text("|", strip=True)
                    texts2 = texts2.split("|")
                    # print(texts2)
        # ---> here text_temp = [Market Cap ,Ex-Dividend Date, 1y Target Est]
                    text_temp = [texts2[1], texts2[-3], texts2[-1]]
                    texts2 = text_temp
                else:
                    texts2 = []
            except IndexError:
                texts2 = []

            return texts2

        def web_content_div(web_content, class_path, value):

            web_content_div = web_content.find_all('div', {'class': class_path})
            try:
                if value != 'None':
                    spans = web_content_div[0].find_all(value)
                    texts = [span.get_text() for span in spans]
                else:
                    texts = []
            except IndexError:
                texts = []

            return texts

        def real_time_price(stock_code):

            Error = 0
            # https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch
            url = 'https://finance.yahoo.com/quote/' + \
                stock_code + '?p=' + stock_code + '&.tsrc=fin-srch'

            try:
                r = requests.get(url)
                web_content = BeautifulSoup(r.text, 'lxml')

                #  prices and Price Change
                texts = web_content_div(
                    web_content, 'D(ib) Mend(20px)', 'fin-streamer')
                # print(texts)
                if texts != []:
                    price, change = texts[0], texts[1] + '' + texts[2]
                else:
                    Error = 1
                    price, change = ['-'], ['-']

                # print("price, change --> ",price,change)

        # ---------->text1 for table-1  content for ->  Previous,Open ,Day_Range, w52_Week_Range ,Volume, Avg_Volume

                texts1 = web_table1(
                    web_content, "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)", "None1")
                # print(texts1)
                if texts1 != []:
                    Previous, Open, Day_Range, w52_Week_Range, Volume, Avg_Volume = texts1[
                        0], texts1[1], texts1[2], texts1[3], texts1[4], texts1[5]
                else:
                    Error = 1
                    Previous, Open, Day_Range, w52_Week_Range, Volume, Avg_Volume = ['-'], ['-'], ['-'], ['-'], ['-'], ['-']
                # print("Previous,Open ,Day_Range, w52_Week_Range ,Volume, Avg_Volume --> ",Previous,Open ,Day_Range, w52_Week_Range ,Volume, Avg_Volume)

        # ----------> for table-2  content for ->  Market_Cap ,Ex_Dividend_Date, one_y_Target_Est

                texts2 = web_table(
                    web_content, "D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)", 'None')
                if texts2 != []:
                    Market_Cap, Ex_Dividend_Date, one_y_Target_Est = texts2[0], texts2[1], texts2[2]
                else:
                    Error = 1
                    Market_Cap, Ex_Dividend_Date, one_y_Target_Est = ['-'], ['-'], ['-']
                # print("Market_Cap ,Ex_Dividend_Date, one_y_Target_Est  --> " ,Market_Cap ,Ex_Dividend_Date, one_y_Target_Est )

            except (ConnectionError):
                price, change, Market_Cap, Ex_Dividend_Date, one_y_Target_Est = ['-'], ['-'], ['-'], ['-'], ['-'] 
                Previous, Open, Day_Range, w52_Week_Range, Volume, Avg_Volume = ['-'], ['-'], ['-'], ['-'], ['-'], ['-']
                Error = 1
                # print("Connection Error")

            return [stock_code,price, change,   Market_Cap, Ex_Dividend_Date, one_y_Target_Est,    Previous, Open, Day_Range, w52_Week_Range, Volume, Avg_Volume]

        temp = real_time_price(
            StockCode)

        # print(temp)
        DataMatrix.append(temp)
    # print(DataMatrix)
    DataMatrix.pop(0)
    tablehead = ['Stock-code','Price', 'Change',   'Market-Cap', 'Ex-Dividend-Date', 'One-yr-Target-Est',    'Previous', 'Open', 'Day-Range', '52-Week-Range', 'Volume', 'Avg-Volume']
    return (DataMatrix,tablehead)

# Stocklist = ['AAPL','MSFT','META']
stock_table_data()
# ans = stockdata(Stocklist)
# print(ans)