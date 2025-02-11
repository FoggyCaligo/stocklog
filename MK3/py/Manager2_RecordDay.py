import pandas as pd

class Manager_Record_Day:
    def __init__(self):
        self.isNew = False
        self.record_day = None
        #record_day.csv 읽어오기 || 파일이 없을 경우 생성
        try:
            self.record_day = pd.read_csv('./csv/record_day.csv')
        except:
            pd.DataFrame(columns=['date','startBudget','rev','revPer','exceed', 'input','endBudget']).to_csv('./csv/record_day.csv',index=False)
            self.isNew=True

    def search_record(self,startDay,endDay):
        return self.record_day[(self.record_day['date'] >= startDay) & (self.record_day['date'] <= endDay)]

    def add_record(self,startBudget,rev,inputValue):
        record = pd.DataFrame(columns=['date','startBudget','rev','revPer','exceed', 'input','endBudget'])

        record['date'] = pd.Timestamp.now().strftime('%Y-%m-%d')
        record['startBudget'] =  inputValue if self.isNew else self.record_day['endBudget'].iloc[-1]
        record['rev'] = rev
        record['revPer'] = rev/record['startBudget']*100
        record['exceed'] = 0
        record['input'] = inputValue
        record['endBudget'] = record['startBudget'] + rev + inputValue
        
        self.record_day = self.record_day.append(record,ignore_index=True)
        self.record_day.to_csv('./csv/record_day.csv',index=False)
        return self.record_day




manager_record_day = Manager_Record_Day()
print(manager_record_day.search_record('2021-01-01','2025-02-06'))
            
