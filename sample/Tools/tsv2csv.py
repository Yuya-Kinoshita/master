import pandas as pd

infile = "../1911/data/sample1.rtf"
outfile = infile.replace(".rtf", ".csv")

data = pd.read_csv(infile, delim_whitespace=True)
data.to_csv(outfile, index=False)
