if __name__ == "__main__":
  a = [1, 2, 1, 2, 1]
  print(max(a, key=a.index))
  print(a.index(max(a)))

  a = 0
  b = 1

  print(b/a if a != 0 else 0)

  c = None
  print(c == None)