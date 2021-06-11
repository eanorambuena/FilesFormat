global shots=1024

def settings(command: str,param):
  t=""
  if command=="host":
    t0="backend=Aer.get_backend('"+param+"')\n"
    t1="job=execute(circuit, backend, shots="+shots+")\n"
    t2="result=job.result()\n"
    t3="counts=result.get_counts(circuit)\n"
    t=t0+t1+t2+t3
  elif command=="shots":
    global shots=param
  elif command=="hist":
    t1="graph=plot_histogram(counts)\n"
    t2="display(graph)\n"
  return t
