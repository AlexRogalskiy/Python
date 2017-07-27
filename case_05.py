import pandas as pd
print pd.__version__

#Load data
#------------------------------------------
df = pd.read_csv("Data.csv")
df.to_csv("Data_copy.csv")

df = pd.read_excel("Data.xlsx", "Sheet1")
df.to_excel("Data_copy.xlsx", sheet_name="Sheet1")

#Dataframe preview
#------------------------------------------
df.head(5)
df.tail(5)
df.columns()

#Rename columns
#------------------------------------------
df2 = df.rename(columns={'ID':'EMPID'})
df2 = df.rename(columns={'ID':'EMPID'}, inplace=True)

#Select columns/rows
#------------------------------------------
df[['ID', "Gender"]]
df[df['Sales'] > 10 & df['BMI'] > 1000]

#Handle missing values
#------------------------------------------
df.dropna()

df.fillna(value=5)
mean = df['Sales'].mean()
df['Sales'].fillna(mean)

#Creat column
#------------------------------------------
df['Sales_Rate'] = df['Sales'] * 40;

#Aggregate data
#------------------------------------------
df.groupby('Gender').sum()

pd.pivot_table(df, values='Sales', index=['Income', 'Product'], columns=['Gender'])
pd.pivot_table(df, values='Sales', index=['Income', 'Product'], columns=['Gender'], aggfunc=len)

pd.crosstab(df['Gender'], df['Income'])

#Merge dataframes
#------------------------------------------
pd.concat([df1, df2])

pd.merge(df1, df2, on='ID', how='inner')

#Apply function
#------------------------------------------
df['Income'].map(lambda x: 10 + x)
df[['Sales','Income']].apply(sum)

func = lambda x: x + ''
df.applymap(func)

#Identify unique values
#------------------------------------------
df['ID'].unique()

#Basic stattistics
#------------------------------------------
df.describe()

df.cov()
df.corr()
