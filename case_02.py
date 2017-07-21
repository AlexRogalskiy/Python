import pandas as pd

#Load data
#------------------------------------------
df = pd.read_csv("Data.csv")
print df.head(3)

df = pd.read_excel("Data.xlsx", "Sheet1")
df = pd.read_csv("Data.txt", sep='\t')

#Load data
#------------------------------------------