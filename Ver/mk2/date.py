from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re
import copy

#전역 변수 : 오늘날짜
today = datetime.now()

#전역함수 : 입력 나누기 
def split_input(input):
    # input = ' ' + input
    print(input.split('.'))
    return input.split('.')


class Date:
    def __init__(self):
        pass

    def get_datetime(self,input):
        rsult = []
        sp = split_input(input)

        #년
        if(sp[0]==''): rsult.append(today.year)
        else: rsult.append(int(sp[0]))
        #월
        if(sp[1]==''): rsult.append(today.month)
        else: rsult.append(int(sp[1]))
        #일
        if(sp[2]==''): rsult.append(today.day)
        else: rsult.append(int(sp[2]))
        return datetime(year=rsult[0], month=rsult[1], day=rsult[2])
    
    def get_periodtime(self,input):
        rsult = []
        input = ' '+input
        sp = split_input(input)
        #년
        if(sp[0]==''): rsult.append(0)
        else: rsult.append(int(sp[0]))
        #월
        if(sp[1]==''): rsult.append(0)
        else: rsult.append(int(sp[1]))
        #일
        if(sp[2]==''): rsult.append(0)
        else: rsult.append(int(sp[1]))
        return relativedelta(years=rsult[0], months=rsult[1], days=rsult[2])
    
    def get_today(self):
        return today.strftime('%Y-%m-%d')



class DateManager:
    def __init__(self):
        self.date = Date()
        self.start = today#시작날짜
        self.end = today#종료날짜

    def get_exact_date(self,input):#시간+- 적용
        if('+' in input):
            sp = input.split('+')
            return self.date.get_datetime(sp[0])+self.date.get_periodtime(sp[1])
        elif('-' in input):
            sp = input.split('-')
            return self.date.get_datetime(sp[0]) - self.date.get_periodtime(sp[1])
        else:
            return self.date.get_datetime(input)

    def get_start_end(self,input):#시작,종료날짜 얻기
        sp = input.split(' ')
        self.start = self.get_exact_date(sp[0])
        self.end = self.get_exact_date(sp[1]) + relativedelta(hours=23)
        print(self.start,self.end)
        return [self.start,self.end]


    def get_today(self):
        return str(today.strftime('%Y-%m-%d'))

    def reform_date(self,input):
        sp = input.split('-')
        return datetime(year=sp[0], month=sp[1], day=sp[2])


    # def gen_dateArr(self):
    #     start = copy.deepcopy(self.start)
    #     end = copy.deepcopy(self.end)
    #     curr = copy.deepcopy(self.start)
    #     rsult = []
    #     while(curr<=end):
    #         rsult.append(curr.strftime('%Y-%m-%d'))
    #         curr = curr+ relativedelta(days=+1)
    #     print('dataarray',rsult)
    #     return rsult
        

# dtMnger = DateManager()
# split_input('..1')
# i = input()
# dtMnger.get_start_end(i)
# print(dtMnger.start, dtMnger.end)