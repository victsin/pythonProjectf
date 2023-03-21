import pandas as pd

df = pd.read_csv("finance_liquor_sales.csv")
print(df.columns)
df1 = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
print(df1)
df_popular = df1.groupby('zip_code').idxmax()
print(df_popular)
df2 = df.groupby('store_number')['bottles_sold'].sum()
total_sales = df2.sum()
df_percentage = (df2 / total_sales) * 100
