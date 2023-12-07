import pandas as pd
dt = pd.read_csv('bank-full.csv', sep=';', header=0)

# print(df.head(5))
print(dt.describe())