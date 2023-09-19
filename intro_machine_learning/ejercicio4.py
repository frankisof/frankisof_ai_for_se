import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
y=home_data.SalePrice
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
x = home_data[feature_names]
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(x, y)
iowa_model.predict(x)

from sklearn.model_selection import train_test_split as tts

train_X, val_X, train_y, val_y = tts(x,y,random_state=1)
print(tts(x,y,random_state=1))
print('\n')
iowa_model = DecisionTreeRegressor(random_state=1)
print(iowa_model.fit(train_X,train_y))
print('\n')
val_predictions = iowa_model.predict(val_X)
print (val_predictions)
print('\n')
from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y,val_predictions)
print(val_mae)
