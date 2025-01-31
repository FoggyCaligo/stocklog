import pandas as pd

class FileManager:
 def __init__(self):
  self.record = pd.read_csv('file/record.csv')
  self.df = pd.DataFrame(record)
  
 
