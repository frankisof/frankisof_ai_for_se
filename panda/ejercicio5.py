import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print("Setup complete.")

print('\n')
dtype = reviews.points.dtype
print(dtype)
print('\n')
point_strings = reviews.points.astype(str)
print(point_strings)
print('\n')
n_missing_prices = pd.isnull(reviews.price).sum()
print(n_missing_prices)
print('\n')
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)
