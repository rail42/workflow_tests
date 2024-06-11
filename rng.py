from random import randint

def randomFromRange(min, max):
  if (max < min):
    return -1
  else:
    return randint(min, max)

