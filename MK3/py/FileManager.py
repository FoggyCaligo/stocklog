import pandas as pd

class FileManager:
    def __init__(self):
        self.isNew=False
        self.record_day = None
        try: 
            self.record_day = pd.read_csv('./csv/record_day.csv')
        except:
            pd.DataFrame(columns=['date','startBudget','rev','revPer','exceed', 'input','endBudget']).to_csv('./csv/record_day.csv',index=False)
            self.isNew=True

    def search_record(self,startDay,endDay):
        return self.record_day[(self.record_day['date'] >= startDay) & (self.record_day['date'] <= endDay)]