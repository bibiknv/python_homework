import pandas as pd

df = pd.read_csv('salary_data.csv', sep=';', index_col=0)
df = df.groupby(['company_name']).mean().reset_index()
df = df.sort_values(['salary', 'company_name'])
df['company_name'].to_csv('sorted_salary', header=False, index=False)
