import pandas as pd

df = pd.read_csv('grades.csv', sep=';', index_col=0)
print(df)
