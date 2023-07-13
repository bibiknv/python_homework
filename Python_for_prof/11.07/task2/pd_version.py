import pandas as pd

df = pd.read_csv('prices.csv', sep=';', index_col=0).unstack()
df_min = df[df == df.min()]
res = df_min.reset_index().sort_values(['level_0', 'Магазин']).reset_index().iloc[0]

#print(res['level_0'] + ': ' + res['Магазин'])

df.to_csv('new_prices.csv', sep=';')
