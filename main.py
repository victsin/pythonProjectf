import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finance_liquor_sales.csv")
print(df.columns)
df1 = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()
df_popular = df1.groupby('zip_code').apply(lambda x: x.loc[x['bottles_sold'].idxmax()])
df_popular = df_popular.reset_index(drop=True)

df2 = df.groupby('store_number')['bottles_sold'].sum()
total_sales = df2.sum()
df_percentage = (df2 / total_sales) * 100
df_popular.to_csv('popular.csv')
df_percentage.to_csv('percentage.csv')

