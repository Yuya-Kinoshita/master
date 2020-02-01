def func(x):
    """
    2次間数
    :param x:
    :return:
    """
    return x ** 2 + 3 * x + 5


def main():
    print(diff(func, -1.5))
    print(gradient_desent(func, 7))


def gradient_desent(f, init_x, lr=0.01):
    """
    1000 回数値微分を計算し，極小値を計算する。
    :param f: 関数
    :param init_x: x の初期値
    :param lr: 学習効率パラメータ
    :return: 極小値
    """
    x = init_x
    for i in range(1000):
        grad = diff(f, x)
        x -= lr * grad
    return x


def diff(_func, x, dx=0.0001):
    """
    関数を微分する
    :param func: 微分する関数
    :param x: x
    :return: x における傾き
    """
    return (_func(x + dx) - _func(x)) / dx


if __name__ == "__main__":
    main()
