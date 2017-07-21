#pip install pandas
#pip install xlrd

import pandas as pd
print pd.__version__

#Load data
#------------------------------------------
# pd.read_csv(filepath, sep=, header=, names=, skiprows=, na_values= ... )
df = pd.read_csv("Data.csv")
print df.head(3)

df = pd.read_excel("Data.xlsx", "Sheet1")
df = pd.read_csv("Data.txt", sep="\t")

#Convert to Date
#------------------------------------------
from datetime import datetime
char_date = 'Apr 1 2017 2:40 PM'
date_obj = datetime.strptime(char_date, "%b %d %Y %I:%M %p")

#Transpose dataset
#------------------------------------------
df.pivot(index='ID', columns='Product', values='Sales')

#Sort dataframe
#------------------------------------------
df.sort(['Product', 'Sales'], ascending=[True, False])

#Generate frequency table
#------------------------------------------
test = df.groupby(['Gender','BMI'])
test.size()

#Generate sample dataset
#------------------------------------------
import numpy as numpy
from random import sample
rindex = np.array(sample(xrange(len(df)), 5))
dfr = df.ix[rindex] # get 5 random rows

#Remove duplicate values
#------------------------------------------
rem_dup = df.drop_duplicates(['Gender','BMI'])

#Group dataset
#------------------------------------------
test = df.groupby(['Gender'])
test.describe()

#Treat missing values
#------------------------------------------
df.isnull()

meanAge = np.mean(df['Age'])
df['Age'] = df['Age'].fillna(meanAge)

#Merge datasets
#------------------------------------------
pd.merge(df1, df2, how='inner', left_index=True, right_index=True)

#SQL connection
#------------------------------------------
import sqlite3
from pandas.io import sql

conn = sqlite3.connect('data.db')
query = "SELECT * FROM data WHERE 'Gender' = 'F';"
results = pd.read_sql(query, con=conn)
print results.head()

#Creating series
#------------------------------------------
# Series(numpy-array, index = )
Series([21, 42, -31, 85], index=['d', 'b', 'a', 'c'])

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100, 'Austin': 450, 'Boston': None}
cities = pd.Series(d)

my_series = Series(np.random.randn(5))
my_series.values
my_series.index
my_series.index.name = 'row.names'

my_series = Series(np.arange(50, 71, 5), index = list('abcde'))
my_series['a']                  # slice using index label
my_series[['a', 'c', 'e']]      # slicing using a list of labels
my_series[0:3]                  # positional slicing
my_series[my_series > .60]      # slicing using a boolean

my_series * 2
np.sqrt(my_series)

index2 = ['a', 'd', 'e', 'f', 'g']
my_series2 = my_series[index2]; my_series2

my_series2.isnull()        # or pd.isnull(my_series2)
my_series2.notnull()       # or pd.notnull(my_series2)

#Creating dataframes
#------------------------------------------
# DataFrame(data=, index=, columns=)
my_df = DataFrame(np.arange(20, 32).reshape(3, 4),
                  columns = ['c1', 'c2', 'c3', 'c4'],
                  index = list('abc'))

my_dict = {'ints': np.arange(5),
           'floats': np.arange(0.1, 0.6, 0.1),
           'strings': list('abcde')}
my_df2 = DataFrame(my_dict, index = list('vwxyz'))

my_df2['const'] = np.pi
my_df2
del my_df2['const']

my_df2.drop(['x', 'y'])                              # delete rows
my_df2.drop(['const', 'ints'], axis=1)               # delete columns

data = {'country': ['Belgium', 'France', 'Germany', 'Netherlands', 'UK'],
        'population': [11.3, 64.3, 81.3, 16.9, 64.9],
        'area': [30510, 671308, 357050, 41526, 244820],
        'capital': ['Brussels', 'Paris', 'Berlin', 'Amsterdam', 'London']}
countries = pd.DataFrame(data)
countries.index            # Check row names
countries.columns          # Check column names
countries.dtypes           # Check data types
countries.info             # Gives overview of the dataset

countries = countries.set_index('country')

countries.sort('population', ascending=False)

#line’ (default), ‘bar’, ‘barh’, ‘hist’, ‘box’ , ‘kde’, ‘area’, ‘pie’, ‘scatter’, ‘hexbin’
countries['population'].plot(kind='bar')                        # barcharts
countries.plot(kind='scatter', x='population', y='area')        # scatterplots

# Using a row index (before comma) and a column name (after comma)
countries.loc['Germany', 'area']

# Using a row index splice and a column index splice
countries.loc['France':'Germany', :]

# Using a boolean for rows and a list of column names
countries.loc[countries['population']>5, ['capital', 'area']]

# Using splices for both rows and columns
countries.iloc[0:2, 1:3]

print my_df2.ix[:, 'strings']                # select a column by name
print my_df2.ix[:, ['strings', 'floats']]   # select multiple columns by name
print my_df2.ix[:, 0:2]                      # select columns by position

print my_df2.ix[0]              # first row
print my_df2.ix[2]              # second row
print my_df2.ix[0:2]           # by position: returns the first 2 rows
print my_df2.ix['x':'z']         # by index: returns the last three rows

#Sort data
#------------------------------------------
s9 = Series(np.random.randn(5), index=list('dcbae')); print s9

s9.sort_index()                 # Sorting on the index 
s9.order(ascending=False)       # Sorting on the values


d9 = DataFrame(np.random.randn(9).reshape(3,3),
               index=list('cba'),
               columns=list('prq'))
print d9
# without arguments, sort_index() will sort the index (rows) of the DataFrame
d9.sort_index()
# To sort column names
d9.sort_index(axis=1)
# Sort the data by the values of a column
d9.sort_index(by='p')
# Sort the data by the values of 2 columns
d9.sort_index(by=['p', 'r'], ascending=False)

#Missing values
#------------------------------------------
# Create a string Series and set some values to missing
s12 = Series(['abc', 'pqr', np.nan, 'xyz', np.nan, 'ijk', None])
# Detect missing values
s12.notnull()
# Replace missing values with a string
s12.fillna('--missing--')

# Create a numeric Series
s13 = Series(np.random.randn(8), index=list('abcdefgh'))
# set a few values to missing
s13[::2] = np.nan
# Fill with median
s13.fillna(s13.median()) #s13.mean()

# Descriptive Statistics
#------------------------------------------
d11 = DataFrame(np.random.randn(25).reshape(5,5),
index=list('abcde'),
columns=list('vwxyz')); print df8
# Getting colsums is as simple as calling the .sum() method of a DataFrame
d11.sum()
# For rowsums, pass axis=1 to the .sum() method
d11.sum(axis=1)
# Find the min/max for each column/row
d11.min(axis=0)            # by column
d11.min(axis=1)      # by row
# Find the location of the min value across rows
d11.idxmin()
# Calculate quantiles for each column
d11.quantile([0.2, 0.4, 0.6, 0.8])

# Categorical Data
#------------------------------------------
# Getting distinct values in a Series
s12 = Series(list('the quick brown fox jumped over the lazy dog'))
s12.unique()
  # Can also use: set(s12)

# Getting a Frequency Table
s12.value_counts()

# isin returns a boolean indicating the position where a match occurred
colours = Series(['red', 'blue', 'white', 'green', 'black', 'white', None])
colours.isin(['white'])

#- count of non-null values,
#- the number of unique values,
#- the mode of the data
#- the frequency of the mode
colours.describe()

#Group dataset
#------------------------------------------
# Create a toy dataset with 2 categorical and 2 numeric variables
df = DataFrame({'k1': list('abcd' * 25),
                'k2': list('xy' * 25 + 'yx' * 25),
                'v1': np.random.rand(100),
                'v2': np.random.rand(100)})
print df.head(15)

# Since k1 has 4 categories, this will return 4 rows
print '\n', df.groupby('k1').mean()

# Since k2 has 2 categories, this will return 2 rows
print '\n', df.groupby('k2').sum()

# A dataframe with a hierarchical index formed by a combination of the levels
print df.groupby([df['k1'], df['k2']]).sum()

# Summing a Series
df['v1'].groupby(df['k1']).sum()

# Summing all Series of a DataFrame
print df.groupby('k2').mean()

# Summing a Series
df['v1'].groupby(df['k1']).agg('sum')

# Finding the mean of all grouped series of a DataFrame
print df.groupby(df.k1).agg('mean').add_prefix('mu_')

# Apply min, mean, max and max to v1 grouped by k1
df['v1'].groupby(df['k1']).agg(['min', 'mean', 'max'])

# Apply min and max to all numeric columns of df grouped by k2
print df[['v1', 'v2']].groupby(df['k2']).agg(['min', 'max'])
     # Hierarchical index will be created

# We can call .stack on the returned object!
print '\n', df[['v1', 'v2']].groupby(df['k2']).agg(['min', 'max']).stack()

# Provide names for the aggregated columns
df[['v1', 'v2']].groupby(df['k1']).agg([('smallest','min'), ('largest', 'max')])

# Apply max and min to v1; and mean and sum to v2; all grouped by k1
df[['v1', 'v2']].groupby(df['k1']).agg({'v1': ['max', 'min'], 'v2': ['mean', 'sum']})

#  Retrieve the top N cases from each group
def topN(data, col, N):
     return data.sort(columns=col, ascending=False).loc[:, col].head(5)
print df.groupby(df['k2']).apply(topN, col='v1', N=5)

#Merge datasets
#------------------------------------------
#merge(df1, df2,
#     how='left', on='key', left_on=None, right_on=None,
#     left_index=False, right_index=False,
#     sort=True, copy=True,
#     suffixes=('_x', '_y'))

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': np.random.randn(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': np.random.randn(3)})

df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data3': np.random.randn(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data4': np.random.randn(3)})

print df1, '\n\n', df2, '\n\n', df3, '\n\n', df4

pd.merge(df1, df2) #pd.merge(df1, df2, on='key')
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

pd.merge(df1, df2, how='outer')
# the merged dataset will have a union of the keys, imputing NaNs where values aren't found
pd.merge(df1, df2, how='left')
# value 'c' is absent in df2, so there will be a NaN in column data2

# Add a column with the same name to df1 and df2
df1['colx'] = np.random.randn(7)
df2['colx'] = np.random.randn(3)

# Specifying suffixes to identify columns with the same name
pd.merge(df1, df2, on='key', suffixes=['_l', '_r'])

# Set lkey to be the index of df3
df3.set_index(lkey, inplace=True)

pd.merge(df2, df3, how='left', left_on='key', right_index=True)

#Combine multiple datasets
#------------------------------------------
# Create toy Series with non-overlapping indices
s1 = Series(np.random.randn(3), index=list('abc'))
s2 = Series(np.random.randn(4), index=list('defg'))
s3 = Series(np.random.randn(2), index=list('hi'))

# Default action is to append the data
pd.concat([s1, s2, s3])
# concat with axis=1 (non-overlapping index)
pd.concat([s1, s2, s3], axis=1)

# Passing keys= creates a hierarchical index when appending (axis=0)
pd.concat([s1, s2, s3], axis=0, keys=['one', 'two', 'thr'])

# Passing keys= gives names to columns when using axis=1
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'thr'])

s4 = Series(np.random.randn(5), index=list('abcde'))
# concat with overlapping index (default join type is outer)
pd.concat([s1, s4], axis=1)
# if we specify a join type, this will be equivalent to a merge
pd.concat([s1, s4], axis=1, join='inner')

# Create toy dataframes with non-overlapping indexes
df1 = DataFrame(np.random.randn(9).reshape(3, 3),
                index=list('abc'), columns=list('XYZ'))
df2 = DataFrame(np.random.randn(4).reshape(2, 2),
                index=list('pq'), columns=list('XZ'))
print df1, '\n\n', df2

#When there is no overlap in indices of the two dataframes, using
# -axis = 0 will produce a concatenation
# -axis = 1 will produce as merge
# No overlapping index
print 'When axis=0 \n'
print pd.concat([df1, df2], axis=0)
print '\n When axis=1 \n'
print pd.concat([df1, df2], axis=1)

# Create toy dataframes with overlapping indexes
df1 = DataFrame(np.random.randn(9).reshape(3, 3),
                index=list('abc'), columns=list('XYZ'))
df2 = DataFrame(np.random.randn(4).reshape(2, 2),
                index=list('ac'), columns=list('XZ'))
print df1, '\n\n', df2

# When axis=0 there will still be
pd.concat([df1, df2])

# Overlapping indexes will be merged
pd.concat([df1, df2], axis=1)

pd.concat([df1, df2], axis=1, keys=['lev_1', 'lev_2'])
# This will create a hierarchical index

#Reshape data
#------------------------------------------
# Create a toy DF with a Hierarchical Index
df = DataFrame(np.random.randn(4, 2),
               index=[list('AB'*2), list('CDEF')],
               columns=list('XY'))
df.index.names = ['one', 'two']
print df

stacked = df.stack()
print stacked

unstacked = stacked.unstack()
print unstacked

#Reshape Data – pivot() and pivot_table()

# Set up a toy dataframe
df = DataFrame({'date': (list(pd.date_range('2000-01-03', '2000-01-05')) * 4),
               'item': (list('ABCD'*3)),
               'status': (np.random.randn(12))})
df.pivot(index='date', columns='item', values='status')

df = pd.DataFrame({'C1':list(('x' * 4 + 'y' * 4)*2),
                   'C2':list('abbbaabaabbbaaba'),
                   'N1':np.random.randn(16)})
print df.pivot_table(index='C1',
                     columns='C2',
                     values='N1',
                     aggfunc='mean')

#Remove Duplicates
#------------------------------------------
df = DataFrame({'C1': list('ABC' * 2),
                'C2': [1, 2, 4, 3, 2, 4]})
df.duplicated()

# Creates a boolean series to indicate which rows have duplicates
df[df.duplicated()]
# Retain the rows that have duplicates
df.drop_duplicates()
# Retain the first occurrence of each row (drop dups)
df.drop_duplicates(take_last=True) #df.drop_duplicates(['list-of-columns'])
# Retain the last occurrence of each row (drop dups)
