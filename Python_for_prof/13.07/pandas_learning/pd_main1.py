# https://stepik.org/lesson/518491/step/10?unit=510939

import pandas as pd

df = pd.read_csv('grades.csv', sep=';', index_col=0)
print(df)
