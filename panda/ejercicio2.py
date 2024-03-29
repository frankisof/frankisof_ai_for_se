import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print("Setup complete.")


desc = reviews.description
print (desc)
print('\n')
first_description =  reviews.description.iloc[0]
print(first_description)
print('\n')
first_row = reviews.iloc[0]
print(first_row)
print('\n')
first_descriptions = reviews.description.iloc[:10]
print(first_descriptions)
print('\n')
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]
print(sample_reviews)
print('\n')
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]
print(df)
print('\n')
cols = ['country', 'variety']
df = reviews.loc[:99, cols]
print(df)
print('\n')
italian_wines = reviews[reviews.country == 'Italy']
print(italian_wines)
print('\n')
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]

print(top_oceania_wines)

print('\n')



