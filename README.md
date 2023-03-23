# # python workearly final assignment

step 1: add the database in Workbench 
step 2: I wrote the query:
        use liquorsales;
        show tables;
        select * from finance_liquor_sales
        where date between '2016-01-01 00:00:01' and  '2019-12-31 00:00:00';
step 3: export the result to a csv file as 'finance_liquor_sales.csv' 
step 4: with Python and Pandas to Aggregate the CSV data so we can get the most popular item sold based on zip code 
        df1 = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()
        df_popular = df1.groupby('zip_code').apply(lambda x: x.loc[x['bottles_sold'].idxmax()])
        df_popular = df_popular.reset_index(drop=True)
and percentage of sales per store
        df2 = df.groupby('store_number')['bottles_sold'].sum()
        total_sales = df2.sum()
        df_percentage = (df2 / total_sales) * 100
then saved the new aggregated data to two new csv files
        df_popular.to_csv('popular.csv')
        df_percentage.to_csv('percentage.csv')
Step 5: I created a scatterplot with matplotlib
        'Most popular item based on sold bottles per Zip Code'
