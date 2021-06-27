import nqs.utils as u
from nqs.code import *

def compiler(name: str):
  lines=getLines(name+".nqa")
  T=""
  t=""
  m=0
  T+="from qiskit import QuantumCircuit, execute, Aer\n"
  T+="from qiskit.visualization import plot_histogram,display\n"
  s=0
  command=""
  param=""
  Q=0
  gate=""
  gatecount=0
  qdef=0
  p=Parser()
  for k in lines:
    for i in k:
      if  p.isDeny(i):
        if m==2:
          m=0
        else:
          m=2
      if i==",":
        pass
      elif s==1: #settings mode on
        if i!=" ":
          command+=i
        else:
          s=2
      elif s==2:
        if i!=" " and i!="\n":
          param+=i
        else:
          T+=q.settings(command,param)
          command=""
          param=""
          s=0
      elif i=="$":
        s=1
      elif qdef==1:
        if i=="q":
          Q+=1
        elif i=="\n":
          qdef=2
          T+="circuit=QuantumCircuit("+str(Q)+","+str(Q)+")\n"
      elif qdef==2:
        if i!="\n" and i!=" ":
          gate+=i
        elif i==" ":
          gatecount+=0.5
          T+=q.quantum(gate,gatecount)
          gate=""
        else:
          T+=q.quantum(gate,gatecount)
          gate=""
          gatecount=0
      elif i=="q":
        qdef=1
        Q+=1
  return T

def execute(name: str):
  T=compiler(name)
  py.write(T,name)

def display(T,delta: int =400):
  while True:
    print(T)
    u.sleep(delta)
    u.clearConsole()
