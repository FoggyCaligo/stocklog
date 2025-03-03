from date import DateManager
from dateutil.relativedelta import relativedelta

import pandas as pd
import copy



class FileManager:
    def __init__(self):
        # self.date = Date()
        self.dm = DateManager() 
        #csv 파일 읽기 or 초기화
        self.dir = './Ver/mk2_cp/csv/record.csv'
        self.columns = ['date','code','price','qty']
        try:
            self.df = pd.read_csv(self.dir)
            self.df['date'] = pd.to_datetime(self.df['date'])
        except:
            # pd.write_csv
            data = {
                'date': ['2025-1-1'],
                'code': ['o'],
                'price':[0],
                'qty':[0]
            }
            self.df = pd.DataFrame(data)
            self.df['date'] = pd.to_datetime(self.df['date'])
            self.df.to_csv(self.dir, index=False)
        
    def record(self,input):
        sp = input.split(' ')
        new_row = pd.DataFrame([{'date': self.dm.get_today(), 'code': sp[0], 'price': sp[1],'qty':sp[2] }])
        new_row.set_index('date')
        self.df = pd.concat([self.df, new_row])
        self.df.to_csv(self.dir, index=False)

    def get_data(self,input):#기간에 맞는 데이터만 가져오기
        startend = self.dm.get_start_end(input)
        return self.df[self.df['date'].between(startend[0],startend[1])]

    def __del__(self):
        self.df.to_csv(self.dir, index=False)




