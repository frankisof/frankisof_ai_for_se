import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
y=home_data.SalePrice
print(home_data.SalePrice)
print('\n')
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
x = home_data[feature_names]
print(x)
print('\n')



iowa_model = DecisionTreeRegressor(random_state=1)
print(iowa_model.fit(x, y))
print('\n')


print(iowa_model.predict(x))


