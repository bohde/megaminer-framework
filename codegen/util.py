def members(x):
  for i in dir(x):
    yield getattr(x,i)

def capitalize(str):
  if not str:
    return str
  return str[0].upper() + str[1:]