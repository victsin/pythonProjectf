import pandas as pd

df = pd.read_csv("finance_liquor_sales.csv")
print(df.columns)
df1 = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
df_popular = df1.groupby('zip_code').idxmax()

df2 = df.groupby(['store_number'])['sale_dollars'].sum()
total_sales = df['sale_dollars'].sum()
df_percentage = (df2 / total_sales) * 100
df_popular.to_csv('popular.csv')
df_percentage.to_csv('percentage.csv')

