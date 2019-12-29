import pandas as pd
# series
# dataFrame
'''data = {'apple': [3, 1, 2, 4, 5],
        'orange' : [2, 5, 6, 7, 9]}
df = pd.DataFrame(data)
print(df['apple'])
'''
# Working on real data
df = pd.read_csv('IMDB-Movie-Data.csv', sep=',')
pd.set_option('display.max_columns', 50)
# Reading data from last
print(df.tail(1))
# Reading data from start
print(df.head(1))
# Changing index column
df1 = pd.read_csv('IMDB-Movie-Data.csv', index_col='Title', sep=',')
#print(df1.head(1))
print(df1.info()) # It provides info in dataFrame
# using data shape
print(df1.shape)
'''It is used for cleaning and transforming of data to know how many data rows and columns are droped due to mull'''

# to check duplicate
print(df1.duplicated().sum)
df1.drop_duplicates()
print(df1.shape)

''' Column Clean up'''

print(len(df1.columns))
# printing columns
print(df1.columns)
# stats of data
print(df1.describe())

# Renaming columns
col = df1.columns
print(list(col))
# Setting new list to change column name
col1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
df1.columns = col1
print(df1.head(1))

# resetting columns name
print('RESET')
df1.columns = col
print(df1.head(1))

# Another method to rename columns
df1.rename(columns={'Runtime (Minutes)': 'Runtime',
                    'Revenue (Millions)': 'Revenue'}, inplace=True)
print(df1.columns)

'''Working with missing values'''
# import numpy
import numpy as np
print(np.nan)
print(df1.isnull().sum())
# Dropping rows
df2 = df1.dropna()
print(df2.shape)

# Dropping whole columns instead of rows

df2 = df1.dropna(axis=1)
print(df2.head())

# Filling na with some value

df2 = df1.fillna(0)
print(df2.isna().sum())

''' filling null value in proper way'''

# Imputation : conventional way to introduce features to null values usually mean or medians
print(df1.isnull().sum())
# extracting revenue data
revenue = df1['Revenue']
# calculating revenue mean
revenue_mean = revenue.mean()
#filling revenue nan with mean
revenue.fillna(revenue_mean, inplace=True)
print(revenue.tail())
print(revenue.isnull().sum())
#replacing updateing revenue
df1['Revenue'] = revenue
print(df1.isnull().sum())

'''Doing same for the meta score'''

metascore = df1['Metascore']

meta_mean = metascore.mean()
metascore.fillna(meta_mean, inplace=True)
print(metascore.isnull().sum())
df1['Metascore'] = metascore
print(df1.isnull().sum())

'''dECRIBE() PROVIDES SUMMARY OF DATA OF NUMBER COLUMNS'''
#describe for whole data
print(df1.describe())
# describe for specific columns
print(df1['Genre'].describe())

'''To know no. of diffrent types of variables'''
print(df['Genre'].value_counts().head(10))

'''Finding unique values'''
print(df1['Genre'].unique())
print(len(df1['Genre'].unique()))


''' Finding co-relation'''
#corr method
cormat = df1.corr()
print(cormat)


'''Ploting with Seaborn'''

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(cormat)
# scatter plot b/w revenue and rating using matplot
plt.figure()
df1.plot(kind='scatter', x='Rating', y='Revenue', title='Revenue vs Rating')
#distributing of rating i.e histogram
plt.figure()
df1['Rating'].plot(kind='hist', title='Rating')
#box plot
plt.figure()
df1['Rating'].plot(kind='box')

plt.show()









