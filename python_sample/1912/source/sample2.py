"""
周波数特性からローパスフィルタのカットオフ周波数を計算する。
R = 1.5 kΩ として電気容量 C を計算する。
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


# 最初にローパスフィルタの関数を定義する。
def low_pass_filter(freq, cut_off):
    """
    ローパスフィルタの周波数特性 (電圧)
    :param freq: 周波数
    :param cut_off: カットオフ周波数 (1 / CR)
    :return: 振幅 (dB)
    """
    # 周波数での減衰率
    ratio = 1.0 / np.sqrt(1 + (freq / cut_off) ** 2)
    # デシベルに変換
    db = 20.0 * np.log10(ratio)
    return db


# データの読み込み
data = np.loadtxt("../data/low_pass_filter_data.csv", skiprows=1, delimiter=",")

# データの減衰比を計算
data_ratio = data[:, 2] / data[:, 1]
# dB に変換
data_db = 20.0 * np.log10(data_ratio)

# フィッティング
par, cov = curve_fit(low_pass_filter, data[:, 0], data_db)
# カットオフ周波数を取得
co = par[0]
# R = 1.5 kΩ を仮定して C を推定
c = 1.0 / (2.0 * np.pi * 1.5e3 * co)
print("C = " + str(c * 1e6) + " uF")
# ベストフィットのデータを作成
# (プロット時になめらかにしたいので，細かく関数のデータを作成する。
best_fit_x = np.arange(data[0, 0], data[-1, 0])  # [0, 0] が周波数の最小値，[-1, 0] が周波数の最大値
best_fit_y = low_pass_filter(best_fit_x, co)

# グラフにプロット -----------------
# y 軸のプロット範囲
y_max = 5
y_min = -50
# グラフ作成
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(data[:, 0], data_db, ".", c="r", label="data")  # データのプロット
ax.plot(best_fit_x, best_fit_y, "-", c="b", lw=1.0, label="best fit")  # ベストフィットのプロット
ax.plot([co, co], [y_min, y_max], "--", c="k", lw=1.0)  # カットオフ周波数に破線を引く
ax.text(co, -45, " {:.1f} Hz".format(co), fontsize=16, ha="left", va="center")  # カットオフ周波数の位置に文字を表示
ax.legend(loc="upper right")  # 凡例を表示 (loc で表示位置を指定)
ax.set_ylim(y_min, y_max)  # y 軸プロット範囲
ax.set_xscale("log")  # x 軸をログスケールに
ax.grid(which="both")  # which: 小さい方の目盛りにもグリッドを引くオプション
ax.set_xlabel("Frequency (Hz)", fontsize=14)  # x 軸ラベル
ax.set_ylabel("dB", fontsize=14)  # y 軸ラベル
ax.set_title("LPF")  # グラフ上部に表示されるタイトル
fig.savefig("../out/low_pass_filter.png")  # グラフを png 形式で保存
