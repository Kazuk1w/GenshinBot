from abc import ABC, abstractmethod
import twder
import requests
from bs4 import BeautifulSoup as BeautifulSoup

# 貨幣抽象類別
class Currency(ABC):
 
    def __init__(self, area):
        self.area = area  # 地區
 
    @abstractmethod
    def Scrape(self):
        pass

class FindCurrency(Currency):

    def Scrape(self):
        # 台銀牌告匯率爬蟲
        if self.area == '美國':
            return float(twder.now('USD')[2])
        elif self.area == '香港':
            return float(twder.now('HKD')[2])
        elif self.area == '英國':
            return float(twder.now('GBP')[2])
        elif (self.area == '澳洲' or self.area == '澳大利亞'):
            return float(twder.now('AUD')[2])
        elif self.area == '加拿大':
            return float(twder.now('CAD')[2])
        elif self.area == '新加坡':
            return float(twder.now('SGD')[2])
        elif self.area == '瑞士':
            return float(twder.now('CHF')[2])
        elif self.area == '日本':
            return float(twder.now('JPY')[2])
        elif self.area == '南非':
            return float(twder.now('ZAR')[2])
        elif self.area == '瑞典':
            return float(twder.now('SEK')[2])
        elif self.area == '紐西蘭':
            return float(twder.now('NZD')[2])
        elif self.area == '泰國':
            return float(twder.now('THB')[2])
        elif self.area == '菲律賓':
            return float(twder.now('PHP')[2])
        elif self.area == '印尼':
            return float(twder.now('IDR')[2])
        elif self.area == '歐洲':
            return float(twder.now('EUR')[2])
        elif (self.area == '韓國' or self.area == '南韓'):
            return float(twder.now('KRW')[2])
        elif self.area == '越南':
            return float(twder.now('VND')[2])
        elif self.area == '馬來西亞':
            return float(twder.now('MYR')[2])
        elif self.area == '中國':
            return float(twder.now('CNY')[2])
        else:
            # Google匯率爬蟲
            if self.area == '烏克蘭':
                CurrencySymbol = 'UAH'
            elif self.area == '緬甸':
                CurrencySymbol = 'MMK'
            else:
                CurrencySymbol = self.area

            url = 'https://www.google.com/finance/quote/' + CurrencySymbol + '-TWD'
            response = requests.request("GET", url)

            try:
                if response.status_code == requests.codes.ok:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    Rate = soup.find('div', 'YMlKec fxKbKc').getText()
                    return Rate
            except:
                return 0
            
