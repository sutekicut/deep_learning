import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

print("test")

class Man:
  def __init__(self, name):
    self.name = name
    print("initialized")

  def hello(self):
    print("Hello " + self.name)

  def goodbye(self):
    print("Goodbye " + self.name)


m = Man("Koudai")

m.hello()
m.goodbye()



# 行列計算
A = np.array([[1, 2], [3, 4]])
print(A)

B = np.array([[3, 0], [0, 6]])
print(B)

print(A * B)



# データの作成
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y)
plt.show()


# matplotlibの使い方を学ぶ
#画像の表示
img = imread("matrix.jpg")
plt.imshow(img)

plt.show()