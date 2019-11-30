import numpy as np

# 入力ファイル名
infile = "data/temperature_190902_191002.csv"
# ファイルの読み込み（skiprows=1 で1行目の読み込みをスキップする)
data = np.loadtxt(infile, delimiter=",", skiprows=1)

# 5 行目を出力
print_row = 4
print(str(print_row + 1) + "行目：", data[print_row])
# 10 行目を出力
print_row = 9
print(str(print_row + 1) + "行目：", data[print_row])

# 4 列目 (最高気温) を出力
print_col = 3
print(str(print_col + 1) + "列目：")
print(data[:, print_col])
# 5 列目 (最低気温) を出力
print_col = 4
print(str(print_col + 1) + "列目：")
print(data[:, print_col])

# 以下、応用
# 10 行目の 4, 5 列目
print_row = 9
print_col_start = 3
print_col_end = 4
print(str(print_col + 1) + "行目の" + str(print_col_start) + "～" + str(print_col_end) + "列")
print(data[print_row][print_col_start:print_col_end + 1])
