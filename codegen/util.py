def members(x):
  for i in dir(x):
    yield getattr(x,i)