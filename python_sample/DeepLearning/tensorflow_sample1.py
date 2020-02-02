import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()


def main():
    """
    勾配降下法で極小値を計算する。
    :return:
    """
    a1 = tf.placeholder(tf.float32)
    b1 = tf.placeholder(tf.float32)

    x1 = tf.Variable(-3.0)
    func = x1 * x1 + a1 * x1 + b1

    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(func)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    for i in range(1000):
        sess.run(train, feed_dict={a1: 3.0, b1: 2.0})

    # 変数の取り出し
    x_r = sess.run([x1])
    print(x_r)


if __name__ == "__main__":
    main()
