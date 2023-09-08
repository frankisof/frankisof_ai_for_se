import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

print("Setup complete.")
reviews_written = reviews.groupby('taster_twitter_handle').size()
print (reviews_written)
print('\n')
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)
print('\n')
price_extremes = reviews.groupby('variety').price.agg([min, max])
print(price_extremes)
print('\n')
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
print(sorted_varieties)
print('\n')
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
print(reviewer_mean_ratings)
print('\n')
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
print(country_variety_counts)
print('\n')


