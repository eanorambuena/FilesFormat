def settings(command: str,param):
  t=""
  if command=="pfcf":
    t="executepfcf(\""+param+"\")"
  elif command=="python":
    t="execute(\""+param+"\")"
  return t