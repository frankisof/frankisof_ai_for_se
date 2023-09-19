import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_absolute_error
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
y=home_data.SalePrice
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
x = home_data[feature_names]
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(x, y)
iowa_model.predict(x)
train_X, val_X, train_y, val_y = tts(x,y,random_state=1)
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X,train_y)
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_y,val_predictions)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
for max_leaf_nodes in candidate_max_leaf_nodes:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    #print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

my_mae = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(my_mae, key=my_mae.get)
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size,random_state=1)

from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X,train_y)
rf_val_mae = mean_absolute_error(val_y,rf_model.predict(val_X))
#print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))



rf_model_on_full_data = RandomForestRegressor(random_state = 0)
rf_model_on_full_data.fit(x,y)
test_data_path = 'test.csv'
test_data = pd.read_csv(test_data_path)
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
test_X = test_data[features] 
test_preds = rf_model_on_full_data.predict(test_X)
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_preds})

output.to_csv('submission.csv', index=False)