import numpy as np

# def  AND(x1, x2):
#   w1, w2, theta = 0.5, 0.5, 0.7
#   tmp = w1 * x1 + w2 * x2
#   if tmp <= theta:
#     return 0
#   elif tmp > theta:
#     return 1

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  if np.sum(w*x) + b <= 0:
    return 0
  elif np.sum(w*x) + b > 0:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-1, -1])
  b = 1

  print(np.sum(w*x))
  print(np.sum(w * x) + b)

  if np.sum(w*x) + b <= 0:
    return 0
  elif np.sum(w*x) + b > 0:
    return 1

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  if np.sum(w*x) + b <= 0:
    return 0
  elif np.sum(w*x) + b > 0:
    return 1

def app():
  print("AND回路")
  print(AND(0, 0))
  print(AND(1, 0))
  print(AND(0, 1))
  print(AND(1, 1))

  print("NAND回路")
  print(NAND(0, 0))
  print(NAND(0, 1))
  print(NAND(1, 0))
  print(NAND(1, 1))

app()