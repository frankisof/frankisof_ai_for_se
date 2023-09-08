import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print("Setup complete.")
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))
print(renamed)
print('\n')
reindexed = reviews.rename_axis('wines', axis='rows')
print(reindexed)

