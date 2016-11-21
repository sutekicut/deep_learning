import unittest

from functools import reduce
print(reduce(lambda x, y: x * y, range(1, 4)))

class TestListMethods:
  def test_filter(self):
    a = ['A', 'J']


    # 11
    b = ['A', '8', '3']







def asterisk(x, y, *move_list):
  print(move_list)
  print(list(move_list))
  print(dict(move_list))

def dict_loop(dictionary: dict):
  for key, value in dictionary.items():
    print("key: {key}  |  value:  {value}".format(key=key, value=value))

if __name__ == '__main__':
  asterisk(1,2,3,4,5,6)
  dict_loop({"book": "週刊少年ジャンプ", "human": "Koudai"})

