import pandas as pd

df = pd.read_csv("finance_liquor_sales.csv")
print(df.columns)
df1 = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
df_popular = df1.groupby('zip_code').idxmax()
df2 = df.groupby('store_number')['bottles_sold'].sum()
total_sales = df2.sum()
df_percentage = (df2 / total_sales) * 100
df_popular.to_csv('popular.csv')
df_percentage.to_csv('percentage.csv')