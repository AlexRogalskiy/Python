import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel("Data.xlsx", "Sheet1")

#Histogram
#------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(df['Age'], bins=7)
plt.title("Age distribution")
plt.xlabel('Age')
plt.ylabel('#Employee')
plt.show()

#Box plot
#------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x.boxplot(df['Age'])
plt.show()

#Violin plot
#------------------------------------------
sns.violinplot(df['Age'], df['Gender'])
sns.despine()

#Bar chart
#------------------------------------------
var = df.groupby('Gender').Sales.sum()
fig = plt.figure();
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Sum of Sales')
ax1.set_title("Gender Sum of Sales chart")
var.plot(kind='bar')

#Line chart
#------------------------------------------
var = df.groupby('BMI').Sales.sum()
fig = plt.figure();
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('BMI')
ax1.set_ylabel('Sum of Sales')
ax1.set_title('BMI Sum of Sales chart')
var.plot(kind='line')

#Stacked column chart
#------------------------------------------
var = df.groupby(['BMI', 'Gender']).Sales.sum()
var.unstack().plot(kind='bar', stacked=True, color=['red','blue'], grid=False)

#Scatter plot
#------------------------------------------
fig = plt.figure();
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df['Age'], df['Sales'])
plt.show()

#Bubble plot
#------------------------------------------
fig = plt.figure();
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df['Age'], df['Sales'], s=df['Income'])
plt.show()

#Pie chart
#------------------------------------------
var = df.groupby('Gender').Sales.sum().stack()
temp = var.unstack()
type(temp)
x_list = temp['Sales']
label_list = temp.index
pyplot.axis("equal") #oval by default
plt.pie(x_list, labels=label_list, autopct="%1.1f%%")
plt.title("Expenses")
plt.show()

#Heat map
#------------------------------------------
data = np.random.rand(4, 2)
rows = list('1234')
columns = list('MF')
fig, ax = plt.subplots()
ax.pcolor(data, cmap=plt.cm.Reds, edgecolors='k')
ax.set_xticks(np.arange(0, 2) + 0.5)
ax.set_yticks(np.arange(0, 4) + 0.5)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.set_xticklabels(columns, minor=False, fontsize=20)
ax.set_yticklabels(rows, minor=False, fontsize=20)
plt.show()