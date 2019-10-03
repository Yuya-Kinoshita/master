import numpy as np

infile = "/Users/yuya/Downloads/data.csv"
data = np.loadtxt(infile, delimiter=",")
print(data)