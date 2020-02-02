import numpy as np


def main():
    print("---AND---")
    print(AND([0, 0]))
    print(AND([0, 1]))
    print(AND([1, 0]))
    print(AND([1, 1]))

    print("---NAND---")
    print(NAND([0, 0]))
    print(NAND([0, 1]))
    print(NAND([1, 0]))
    print(NAND([1, 1]))

    print("---OR---")
    print(OR([0, 0]))
    print(OR([0, 1]))
    print(OR([1, 0]))
    print(OR([1, 1]))


def model(x, w, b):
    val = np.sum(x * w) + b
    if val > 0:
        return 1
    else:
        return 0


def AND(x):
    x = np.array(x)
    w = np.array([0.5, 0.5])
    b = -0.7
    return model(x, w, b)


def NAND(x):
    x = np.array(x)
    w = np.array([-0.5, -0.5])
    b = 0.7
    return model(x, w, b)


def OR(x):
    x = np.array(x)
    w = np.array([0.5, 0.5])
    b = -0.2
    return model(x, w, b)


if __name__ == "__main__":
    main()
