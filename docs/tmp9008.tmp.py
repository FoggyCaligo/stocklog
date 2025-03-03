from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import re









#-----------------------------
class YM:
  def __init__(self,t): #t: type(orig, adj)
    cmd = []
    self.t = t
    self.today = datetime.now()
    self.date = self.today
    self.y = self.today.year
    self.m = self.today.month
  def update(self,cmd,se):
    #get year, month  from cmd
    if(self.t=='orig'): #if target is original
      if re.search('y',cmd): #if 'y' in cmd
        self.y = re.match(r"^[^y]*", cmd).group() # get content before 'y'
        print('y',self.y)
      else: # if 'y' aren't in cmd
        if re.search('m',cmd):
          self.y = self.today.year
          # self.m = re.match(r"^[^m]*",cmd[len(y):-1]).group()
          # print('m',m)
      #transform t(this) into today
      if self.y=='t':
        self.y = self.today.year
      if self.m=='t':
        self.m = self.today.month
    elif self.t=='adj': #if target is adjust value
      if re.search('y',cmd): #if 'y' in cmd
        self.y = re.match(r"^[^y]*", cmd).group() # get content before 'y'
        print('y',self.y)
      else: # if 'y' aren't in cmd
        if re.search('m',cmd):
          self.y = 0
          self.m = re.match(r"^[^m]*",cmd[len(y):-1]).group()
        print('m',m)
            
  def get(self):
    return [self.y,self.m]


#----------------------
class Date_adj:
  def __init__(self):
    self.date = datetime.now();
    pass
    
  def trs(self,cmd):
    if re.search('-',cmd):
      self.adjust(cmd,'-')
    elif re.search('+',cmd):
      self.adjust(cmd,'+')
    
    
  def adjust(self,cmd,op): #ex: [2024y3m,3y4m]
    split = cmd.split(op)

    orig = YM('orig')
    orig.update(split[0])

    adj = YM('adj')
    adj.update(split[1])

    origym = orig.get()
    adjym = adj.get()

    if op=='+':
      rsulty = origym[0] - adjym[0]
      rsultm = origym[1] - adjym[0]

    elif op=='-':
      rsulty = origym[0] + adjym[0]
      rsultm = origym[1] + adjym[1]
      

class Date_Manager:
  def __init__(self):
    pass

  def cmd(self,cmd):
    if re.search('-',cmd):
      
      pass

    elif re.search('+',cmd):
      pass
    
  
      
      

    
    #cmd[0]:TN
    #cmd[1]:YM
    #--------
    #cmd[2]:-+
    #cmd[3]:TN
    #cmd[4]:YM



   
#-------------------
class Date_Manager:
  def __init__(self):
    pass
    
    
      
  #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

timer = Timer()
timer.getCmd('test 1')
# 
# timer.checkTime()
# timer.setTime("s",2021,1,4)
# timer.checkTime()
# timer.initTime('s')
# timer.checkTime()







#------------------------
'''
//biggest split
space = aaa~aaa (aaa aaa)

//value
t = this
N = number

//type
y = year
m = month

//additional
- : minus
+ : plus





show 2024y1m 2024y12m
show ty-1m tm-1m

show tm tm-3
show tm 
show 3m
show 3m + 4m 
'''
