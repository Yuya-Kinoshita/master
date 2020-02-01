import tensorflow as tf


def main():
    # 定数の定義
    a = tf.constant(1)
    b = tf.constant(2)

    # 計算グラフの定義
    c = tf.add(a, b)

    sess = tf.Session()
    # 計算実行
    result = sess.run(c)
    print(result)


if __name__ == "__main__":
    main()
