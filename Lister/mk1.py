import FinanceDataReader as fdr
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta



# 정제된 데이터를 저장할 데이터프레임
df_refined = pd.DataFrame()
# S&P500 종목 리스트
df_sp500 = fdr.StockListing('S&P500')
#변수들
today = dt.datetime.now()
yesterday = dt.datetime.now() - relativedelta(days=1)

#함수들
def dt2Str(date):
    # print(date.strftime('%Y-%m-%d'))
    # return str(date.strftime('%Y-%m-%d'))
    print(f'{date.year}-{date.month}-{date.day}')
    return f'{date.year}-{date.month}-{date.day}'


def format_symbol(symbol):
    special_symbols = {
        'BRKB': 'BRK-B',  # Berkshire Hathaway
        'BFB': 'BF-B',    # Brown-Forman Corp class B
    }
    return special_symbols.get(symbol, symbol)


#메인
for each in df_sp500['Symbol']:

    df = fdr.DataReader(format_symbol(each),dt2Str(yesterday),dt2Str(today))
    print(df)

    # print(df['Close'][-1])
    # print(df['Dividend Yield'][-1])
    # if df['Close'][-1] < 90 and df['Dividend Yield'][-1] >= 0.055:
    #     df_refined = pd.concat([df_refined, df])
    



df_sp500.to_csv('./Lister/sp500.csv')






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

