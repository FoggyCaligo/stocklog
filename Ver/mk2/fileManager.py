import pandas as pd

class FileManager:
    def __init__(self):
        df = pd.read_csv('./Ver/mk2/csv/record.csv')
        print(df)
        pass

fm = FileManager()
