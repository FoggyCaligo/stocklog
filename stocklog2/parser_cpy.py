import csv
from datetime import datetime, timedelta
#from datetime import timedelta as td
from dateutil.relativedelta import relativedelta


class Timer:
 def __init__(self):
  self.start = datetime.now()
  self.end = datetime.now()-relativedelta(months=1)

 def setTime(self,flag,y,m,d):
  if flag=="s":
   self.start = datetime(y,m,d)
  elif flag=="e":
   self.end = datetime(y,m,d)
  else: print("settime() err")
 
 def initTime(self,flag):
  if flag=="s":
   self.start=datetime.now()
  elif flag=="e":
   self.end=datetime.now()-relativedelta(months=1)
  else: print("inittime err")
 
 def checkTime(self):
  print(self.start,self.end)
  
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
class FileManager:
 def __init__(self):
  f=open('record.csv',r)

 def __del__(self):
  f.close()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
class Parser:
 def __init__(self):
  self.cmd1 = ["t","w","s"]
  self.cmd2 = ["s","e"]
  self.cmd3 = "r"
  
 
  self.file = FileManager()
  self.time = Timer()
  self.cmd = ""

 def translate(self, i):
  words = i.split(" ")
  #명령어
  #t  s,e   r,"yyyy mm dd"
  #w
  #s
  if words[0] === self.cmd1[0]:#time set"t"
   if words[1] === self.cmd2[0]:#"s" #start
    if words[2] === self.cmd3:
     self.time.initTime("s")
    else:
     temp = words[3].split(".")#set date ex 2025.1.3
     try:
      self.time.setTime("s", temp[0], temp[1], temp[2])
     except:
      print("wrong cmd.")
   elif words[1]==="e": #end
    

   else:print("unknown time setting target")
   

  elif words[0] ==="w";#write
   pass

  elif words[0] === "s":#show result
   pass
  else: print("wrong cmd")
   
  

 def getCmd(self):
  cmd = input()
  cmd = 
  
  
 
  


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

timer = Timer()

timer.checkTime()
timer.setTime("s",2021,1,4)
timer.checkTime()
timer.initTime('s')
timer.checkTime()


parser = Parser()

