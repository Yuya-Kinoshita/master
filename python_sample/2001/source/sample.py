"""
リアルタイムプロットのサンプルコード
"""
import numpy as np
from matplotlib import pyplot as plt

# リアルタイムプロット機能をON
plt.ion()
# グラフオブジェクトを作成
fig = plt.figure()
ax = fig.add_subplot(111)

# 以下，無限ループでプロット
x = 0
while True:
    # センサーからの値などを取得する。
    # 今回は単純に sin 関数をプロットする。
    x += 0.1
    y = np.sin(x)
    # 値のプロット (値が追加されていく)
    ax.plot(x, y, "r.")
    plt.draw()
    # 0.2 秒待つ
    plt.pause(0.2)
