import FinanceDataReader as fdr
import pandas as pd

import datetime as dt
from dateutil.relativedelta import relativedelta

class Lister:
    def __init__(self):
        self.df_refined = pd.DataFrame()
        self.df_sp500 = fdr.StockListing('S&P500')
        
        self.period = { 'y': 0, 'm': 1, 'd': 0 }
        self.today = dt.datetime.now()
        self.start = dt.datetime.now()
        self.end = self.get_startDate()
        self.startDate = ''
        self.endDate = ''
        
    def set_period(self, period):
        self.period = period
        #적용
        self.start = self.get_startDate()
        self.end = self.get_endDate()
        self.startDate = self.start.strftime('%Y-%m-%d')
        self.endDate = self.end.strftime('%Y-%m-%d')

    def set_date(self, start, end):
        self.start = start
        self.end = end
        #적용
        self.startDate = self.start.strftime('%Y-%m-%d')
        self.endDate = self.end.strftime('%Y-%m-%d')

    #날짜 계산
    def get_startDate(self):        
        return self.today - relativedelta(years=self.period['y'] , months=(self.period['m']),days=(self.period['d']) )
    def get_endDate(self):
        return (self.end)
    def dt2Str(self, date):
        return date.strftime('%Y-%m-%d')
        # return f'{date.year}-{date.month}-{date.day}'



    def get_refined(self):
        for each in self.df_sp500['Symbol']:
            
            df = fdr.DataReader(each, self.startDate, (self.endDate))
            print(df)
            print(df.iloc['Close'][-1])
            print(df.iloc['Dividend Yield'][-1])
            if df.iloc['Close'][-1] < 90 and df.iloc['Dividend Yield'][-1] >= 0.055:
                self.df_refined = pd.concat([self.df_refined, df])
        
        return pd.read_csv('./Lister/sp500.csv')

    def run(self):
        self.get_refined()

    def __del__(self):
        self.df_refined.to_csv('./Lister/refined.csv')


lister = Lister()
lister.set_period({'y': 0, 'm': 0, 'd': 1})
lister.run()

'''
1. s&p500 종목 리스트화
2. 그중 현재가가 x(10만)원 이하인 종목 리스트화
3. 그중 배당수익률이 y(5.5%) 이상인 종목 리스트화

4. -> 뽑힌 리스트에 있는 종목들 보면서 차트괜찮은것들 표시
5. 뽑힌 리스트 다시보기
6. 가장 잘될것 같은 종목들 위주로 5개정도 선정
7. 매수

8.->시세차액이 받을 배당금 이상이면 매도, 아니면 배당금 받기
'''

