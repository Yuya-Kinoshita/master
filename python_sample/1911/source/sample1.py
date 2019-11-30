"""
sample1.py
Python 学習会 11 月分の解答 (1)
sample1.csv ファイルを読み込み，データ解析を行う。
"""

import numpy as np

# 入力ファイル
infile = "../data/sample1.csv"

# CSV ファイルを読み込み (1行目をスキップ)
data = np.loadtxt(infile, skiprows=1, delimiter=",")

# 各教科の平均点，標準偏差，最低点，最高点を求める。
# ループを使う (必ずしも使う必要はない)
# 空の配列 (list) を定義
point_avg = []
point_std = []
point_max = []
point_min = []
# 教科の順番
subject_list = ["Japanese", "English", "math", "physics", "chemistry"]
for i in range(1, len(data[1, :])):  # 1 ~ 5 までのループ (len で配列の長さを取得 => 1 から 1 行目の長さまで)
    # 教科を出力
    print("Subject = " + subject_list[i - 1])
    # 各パラメータを計算
    _avg = np.average(data[:, i])
    _std = np.std(data[:, i])
    _max = np.max(data[:, i])
    _min = np.min(data[:, i])

    # 出力 (改行なし)
    print("average: " + str(_avg), end=" ")
    print("standard deviation: " + str(_std), end=" ")
    print("maximum: " + str(_max), end=" ")
    print("minimum: " + str(_min), end=" ")
    # 改行
    print()
    print()

    # list に各教科ごとの計算結果を追加していく
    point_avg.append(_avg)
    point_std.append(_std)
    point_max.append(_max)
    point_min.append(_min)

# 国語の平均点を別の変数に代入 (わかりやすさのため，省略可)
point_avg_jp = point_avg[0]
# 国語の列のデータを別の変数に代入 (わかりやすさのため，省略可)
point_list_jp = data[:, 1]
# 人 (No.) の列のデータを別の変数に代入 (わかりやすさのため，省略可)
number_list = data[:, 0]

# 国語の点数が平均点以上の No のデータを抽出
point_jp_over_avg = number_list[point_list_jp >= point_avg_jp]
print("Japanese point over average")
print(point_jp_over_avg)

# 合計点の計算
# 空の配列を定義
point_sum = []
# 人 (No.) でループ
for i in range(len(data[:, 0])):
    # 合計を計算して配列に追加
    point_sum.append(np.sum(data[i, :]))
# list を np.ndarray に変換
point_sum = np.array(point_sum)

# 合計点の平均と標準偏差
sum_avg = np.average(point_sum)
sum_std = np.std(point_sum)

# np.ndarray の四則演算で全 No. の偏差値を一気に計算する
# 偏差値 = (10 * (点数 - 平均) / 標準偏差) + 50
hensati = (10 * (point_sum - sum_avg) / sum_std) + 50
print("hensati")
print(hensati)

# 偏差値の分布を計算
# bins=... で棒グラフの区切り幅を指定する。今回は 0 から 100 まで 10 ずつ。
# y がその範囲にある数値の数，x が区切りの境界点
dist_y, dist_x = np.histogram(hensati, bins=range(0, 100, 10))
# np.histogram の仕様で，境界点のほうがデータが一つ多くなるので，y に 0 を追加する。
dist_y = np.append(dist_y, 0)

# データを CSV ファイルに書き出す。
# 書き出すためのデータを作成 (.T で転置する)
out = np.array([dist_x, dist_y]).T
# 出力ファイル
outfile = "../out/sample1_hensati_dist.csv"
# savetxt で書き出す
np.savetxt(outfile, out, delimiter=",")

# 以下，グラフ化。課題とは関係ないので無視してください
# これが原因でこのコードが動かない場合は削除してください。
from matplotlib import pyplot as plt

plt.plot(dist_x, dist_y, ls="steps", color="r", lw=1.0)
plt.grid()
plt.xlim(0, 100)
plt.ylim(0, 20)
plt.show()
