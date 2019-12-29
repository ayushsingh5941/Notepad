import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Testing pandas series data structure
hello = pd.Series(['hello', 'world'])
country = pd.Series(['India', 'America', 'Japan'])
city = pd.Series(['Delhi', 'New York', 'Tokyo'])
population = pd.Series([852469, 1015785, 485199])
# Testing dataframe
combined = pd.DataFrame({'country': country, 'city': city})
# Testing csv operations
ca_housing_dataframe = pd.read_csv('california_housing_train.csv', sep=',')
pd.set_option('display.max_columns', 50)
ca_housing_dataframe.hist('median_house_value')
plt.show()

# Adding another column
combined['city2'] = pd.Series(['Mumbai', 'California', 'Edo'])
print(combined)

