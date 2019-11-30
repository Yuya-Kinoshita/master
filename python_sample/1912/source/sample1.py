"""
課題1: 電圧ー電流のデータから抵抗値 (インピーダンス) を計算する。
"""
import numpy as np
from matplotlib import pyplot as plt

# データの読み込み
data = np.loadtxt("../data/iv_data.csv", delimiter=",", skiprows=1)

# 1 次関数でフィッティング
par = np.polyfit(data[:, 1], data[:, 0], 1)
# フィッティング結果の傾き = 抵抗値 [mΩ]
r = par[0]
print("R = " + str(r) + " mΩ")

# ベストフィットデータの作成
best_fit = par[0] * data[:, 1] + par[1]

# グラフのプロット
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(data[:, 1], data[:, 0], ".", c="r", label="data")  # データ
ax.plot(data[:, 1], best_fit, "-", c="b", label="best fit")  # ベストフィット
ax.set_xlabel("Current (mA)", fontsize=14)  # x 軸ラベル
ax.set_ylabel("Voltage (V)", fontsize=14)  # y 軸ラベル
ax.grid()  # グリッド線
ax.legend(loc="upper left")  # 凡例
fig.savefig("../out/iv.png")  # グラフの保存
