import pandas as pd

df = pd.read_csv('sales.csv', sep=';', index_col=0)
predicat = df['old_price'] > df['new_price']
df[predicat].to_csv('new_prices.csv', sep=';')
