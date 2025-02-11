import pandas as pd
import time
from datetime import datetime as dt

class Manager_Expect:
    #(연,월, 월별입금액, 시작금, 월수익률)
    #날짜 입금액 시작금 수익금 월말보유금

    def __init__(self,start,takeY,takeM, inputValue, startBudget, revPer):
        self.record = pd.DataFrame()#csv
        self.gen(start,takeY,takeM, inputValue, startBudget, revPer)
    def __init__(self,takeY,takeM, inputValue, startBudget, revPer):
        self.record = pd.DataFrame()#csv
        self.gen([2025,1],takeY,takeM, inputValue, startBudget, revPer)

    def getDateRecord(self,date):
        # print(self.conv)
        # return self.conv[str(date)]
        # return self.conv[date]
        # return self.conv.iloc(date)
        print(self.record)
        return self.record[str(date)]


    def gen(self,start,takeY,takeM, inputValue, startBudget, revPer):
        #시작날짜와 종료날짜 추출
        # revPer = revPer/20 #일일 수익률(20영업일 : 1달)
        s = pd.Timestamp(str(start[0])+'-'+str(start[1])+'')
        e = pd.Timestamp(str(start[0]+takeY)+'-'+str(start[1]+takeM)+'')
        #기간내 모든 날짜 데이터 생성
        date_range = pd.date_range(start=s,end=e,freq='MS')
        
        self.pastData = []#past line
        self.pastEndBudget = 0
        #날짜 순회
        for date in date_range:
            #날짜 입금액 시작금 수익금 월말보유금
            # date = str(date)[0:7]
            if(self.pastEndBudget == 0):#첫날
                self.record[str(date)] = [str(date)[0:7],self.AddComma(inputValue), self.AddComma(startBudget), self.AddComma(round(startBudget*revPer/100)), self.AddComma(round(startBudget + startBudget * revPer/100 + inputValue))]
                self.pastEndBudget = round(startBudget + startBudget * revPer/100 + inputValue)
            else:#이후
                self.record[str(date)] = [str(date)[0:7],self.AddComma(inputValue), self.AddComma(self.pastEndBudget), self.AddComma(round(self.pastEndBudget*revPer/100)), self.AddComma(round(self.pastEndBudget + self.pastEndBudget * revPer/100 + inputValue))]
            self.pastEndBudget = round(self.pastEndBudget + self.pastEndBudget * revPer/100 + inputValue)
            # print("test:",str(date)[0:7], type(str(date)[0:7]), type('test'))
        #최종적으로 기록 덮어쓰기
        self.conv = self.record.transpose()
        self.conv.rename(columns=self.conv.iloc[0], inplace=True)
        self.conv = self.conv.drop(self.conv.index[0])

        self.conv.to_csv('./csv/record_expect.csv',index=False)
            
    def show(self):
        print(self.conv)

    def AddComma(self, num):
        if(type(num) == str):
            return format(int(num), ',')
        return format(num, ',')

          
test = Manager_Expect(takeY=10,takeM=0,  inputValue=500000, startBudget=200000, revPer=1)
# test.gen(10,0, 50, 20, 1)
# test.show()
# print(test.search_record('2025-01','2025-05'))
# time.sleep(3)
print(test.getDateRecord('2025-05'))