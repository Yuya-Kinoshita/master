"""
リアルタイムプロットのサンプルコード
q を入力すると終了する。
"""
import threading

import numpy as np
from matplotlib import pyplot as plt

# どちらの関数からも参照できるようグローバル変数として定義
flag = True


def plot():
    # リアルタイムプロット機能をON
    plt.ion()
    # グラフオブジェクトを作成
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # 以下，無限ループでプロット
    x = 0
    global flag
    flag = True
    while flag:
        # センサーからの値などを取得する。
        # 今回は単純に sin 関数をプロットする。
        x += 0.1
        y = np.sin(x)
        # 値のプロット (値が追加されていく)
        ax.plot(x, y, "r.")
        plt.draw()
        # 0.2 秒待つ
        plt.pause(0.2)


def main():
    # プロットスレッドの作成
    plot_thread = threading.Thread(target=plot)
    plot_thread.start()

    # 無限ループで入力待ち
    while True:
        _str = input(">>")
        # 入力が "q" の場合
        if _str == "q":
            global flag
            flag = False
            break
    # スレッドを閉じる
    plot_thread.join()


if __name__ == "__main__":
    main()
