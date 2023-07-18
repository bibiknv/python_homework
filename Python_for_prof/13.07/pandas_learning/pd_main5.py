# https://stepik.org/lesson/518491/step/15?unit=510939

import pandas as pd

index_row = int(input())
df = pd.read_csv('exam.csv', sep=',', index_col=0)

