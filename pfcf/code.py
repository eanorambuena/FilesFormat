import os

def codef(codel: str,text: str): #code function
  file=codel+".compile.py"
  f=open(file,"w")
  t=""
  if codel=="qiskit":
    t=qiskit(text)
  f.write(t)
  f.close()
  #os.remove(file)

def qiskit(text: str):
  t=[]
  t.append("from qiskit import QuantumCircuit, execute, Aer")
  t.append("from qiskit.visualization import plot_histogram")
  T=""
  for i in t:
    T+=i+"\n"
  return T