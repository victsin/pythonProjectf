import pandas as pd

df = pd.read_csv("finance_liquor_sales.csv")
print(df.columns)
df1 = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
print(df1)
df_popular = df1.groupby(level = 0).nlargest(1)
print(df_popular)