import pandas as pd

infile = "../data/data.csv"
outfile = "../data/temperature_190902_191002.csv"

df = pd.read_csv(infile, skiprows=6, header=None)

df.columns = ["date", "max", "a", "b", "min", "c", "d"]
df["date"] = pd.to_datetime(df["date"])
year = []
month = []
day = []
for date in df["date"]:
    year.append(date.year)
    month.append(date.month)
    day.append(date.day)
df["year"] = year
df["month"] = month
df["day"] = day
print(df[["year", "month", "day", "max", "min"]])

df[["year", "month", "day", "max", "min"]].to_csv(outfile, header=None, index=False)
