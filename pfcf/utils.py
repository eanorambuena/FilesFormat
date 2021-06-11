import time, os, json

def getLines(adress: str):
  h=open(adress,"r")
  lines=h.readlines()
  h.close()
  return lines

def sleep(i: int =100):
  time.sleep(i/1000)

def delete(name: str,fileformat:str =".pfcf"):
  os.remove(name+fileformat)

def dump(structure, file):
  json.dump(structure, file, indent=2)

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls    
    command = 'cls'
  os.system(command)