import matplotlib.pyplot as plt
import numpy as np


def main():
    factor = 0.1
    r = 1e3
    v = np.arange(0, 3, 0.2)
    i = [(get_current(i, r) * 1e3 + (np.random.rand() - 0.5) * factor) for i in v]
    plt.plot(i, v, "r.")
    plt.show()
    save_data = np.array([v, i]).T
    outfile = "../1912/data/iv_data.csv"
    np.savetxt(outfile, save_data, delimiter=",")


def get_current(v, r):
    return v / r


if __name__ == "__main__":
    main()
