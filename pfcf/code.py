from pfcf.utils import *
import pfcf.codel.qiskit as q

def codef(codel: str,text: str): #code function
  form=".compile.py"
  f=open(codel+form,"w")
  t=""
  if codel=="qiskit":
    t=qiskit(text)
  f.write(t)
  f.close()
  sleep(1000)
  delete(codel,form)

def qiskit(text: str):
  t=[]
  t.append("from qiskit import QuantumCircuit, execute, Aer\n")
  t.append("from qiskit.visualization import plot_histogram\n")
  T=""
  s=0
  command=""
  param=""
  Q=0
  gate=""
  gatecount=0
  qdef=0
  for i in text:
    if s==1: #settings mode on
      if i!=" ":
        command+=i
      else:
        s=2
    elif s==2:
      if i!=" " and i!="\n":
        param+=i
      else:
        t.append(q.settings(command,param))
        s=0
    elif i=="$":
      s=1
    elif qdef==1:
      if i=="q":
        Q+=1
      elif i=="\n":
        qdef=2
        t.append("circuit== QuantumCircuit("+str(Q)+","+str(Q)+")\n")
    elif qdef==2:
      if i!="\n" and i!=" ":
        gate+=i
      elif i==" ":
        gatecount+=0.5
        t.append(q.quantum(gate,gatecount))
        gate=""
      else:
        t.append(q.quantum(gate,gatecount))
        gate=""
        gatecount=0
    elif i=="q":
      qdef=1
      Q+=1
    
  for i in t:
    T+=i
  return T

