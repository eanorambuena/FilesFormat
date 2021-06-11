from pfcf.utils import *
import pfcf.codel.qiskit as qiskit

def codef(codel: str,text: str): #code function
  form=".compile.py"
  f=open(codel+form,"w")
  t=""
  if codel=="qiskit":
    t=qiskit(text)
  f.write(t)
  f.close()
  sleep(100)
  delete(codel,form)

def qiskit(text: str):
  t=[]
  t.append("from qiskit import QuantumCircuit, execute, Aer")
  t.append("from qiskit.visualization import plot_histogram")
  T=""
  s=0
  command=""
  param=""
  for i in text:
    if s==1: #settings mode on
      if i!=" ":
        command+=i
      else:
        s=2
    elif s==2:
      if i!=" ":
        param+=i
      else:
        qiskit.settings(command,param)
        s=0
    elif i=="$":
      m=1
    
  for i in t:
    T+=i+"\n"
  return T

