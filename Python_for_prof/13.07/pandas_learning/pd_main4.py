# https://stepik.org/lesson/518491/step/14?unit=510939
import pandas as pd

df = pd.read_csv('deniro.csv', sep=',', index_col=0)
number_of_row = int(input())
df_new = df.iloc[:, number_of_row]
print(df_new)
print(df)
