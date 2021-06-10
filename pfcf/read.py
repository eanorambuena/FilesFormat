from pfcf.parser import *

def getLines(adress):
  h=open(adress,"r")
  lines=h.readlines()
  h.close()
  return lines

def read(name,printYesOrNo=1,returnText=0):
  lines=getLines(name+".pfcf")
  T=""
  t=""
  m=0
  p=Parser()
  lineCount=0
  for k in lines:
    count=0
    for i in range(0,len(k)):
      if  p.isDeny(k[i]):
        if m==2:
          m=0
        else:
          m=2
      elif  p.isVip(k[i]):
        m=1
      elif m==2:
        pass
      elif m==1:
        t+=k[i]
        m=0
      elif p.separator(k[i]):
        T+=t+"\n"
        t=""
      elif p.section(k[i]):
        T+="\n"
      elif  p.skip(k[i]):
        pass
      elif k[i]!="\n":
        t+=k[i]
      count+=1
    lineCount+=1
  if printYesOrNo:
    print(T)
  if returnText:
    a={T,k}
    return a
  return T

import time
def executepfcf(name):
  while True:
    T=read(name)
    f=open(name+".txt","w")
    f.write(T)
    f.close()
    time.sleep(0.1)