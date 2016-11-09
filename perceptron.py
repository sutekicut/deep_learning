import numpy as np

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7

  if np.sum(w * x) + b <= 0:
    return 0
  elif np.sum(w * x) + b > 0:
    return 1



def app_main():
  print(AND(0, 0))
  print(AND(1, 0))
  print(AND(0, 1))
  print(AND(1, 1))


app_main()