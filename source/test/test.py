class Test:
  def __init__(self):
    self.value = [[0 for i in range(0, 10)] for j in range(0, 10)]

  #listから、最大値の最初のindexを取得する
  def max_index(self):
    if test:
      a = [1, 2, 1, 2, 1]
      print(max(a, key=a.index))
      print(a.index(max(a)))

  def multiple_sprintf(self):
    if test:
      test_str = "%d: %f, %d: %f," % (1, 2.0, 2, 4.0)
      return test_str

  def max_key(self, arr: dict):
    if test:
      print(arr.items())
      print(max(arr.items()))
      print([(v, k) for (k, v) in arr.items()])
      print(max([(v, k) for (k, v) in arr.items()]))
      print(max((v, k) for (k, v) in arr.items()))

  def multiple_return(self):
    if test:
      return 1, 2

  def print_format(self):
    if test:
      a = 10
      return "  |  %d" * len(range(0, a))

  def zero_division(self):
    if test:
      a = 0
      b = 1
      print(b / a if a != 0 else 0)

  def map_test(self):
    if test:
      value_map = ()
      for i in range(0, 5):
        value_map += tuple(map(lambda j: float(self.value[i][j]), list(range(0, 5))))
        print(value_map)
        # num_list.append()

  def add_tuple(self):
    a = (1,2,3)
    b = (0,) + a
    return b


if __name__ == "__main__":
  test = Test()
  print(test.multiple_sprintf())
  test.map_test()

  print(test.add_tuple())
