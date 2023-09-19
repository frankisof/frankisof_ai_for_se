import pandas as pd

melbourne_file_path = 'melb_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)
print (melbourne_data.describe())


iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
print('\n')
print (home_data.describe())

