import pandas as pd
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

print(fruits)

print('\n')

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])

print(fruit_sales)
print('\n')

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')

print(recipe)
print('\n')
reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
pd.set_option('display.max_rows',5)
print(reviews)
print('\n')

print(" select top 1 country from winesmag")
reviews_country_top1= reviews['country'][2],
print(reviews_country_top1)
print('\n')
print('\n sub-dataset \n select country form winesmag\n')
reviews_country = reviews.iloc[1:3],
print(reviews_country)

print('\n')
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv")


