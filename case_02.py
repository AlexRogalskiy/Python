import pandas as pd

print pd.__version__

#Load data
#------------------------------------------
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
dfr = df.ix[rindex] #get 5 random rows

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
