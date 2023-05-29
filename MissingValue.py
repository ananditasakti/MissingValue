import pandas as pd

cd = pd.read_csv('shopping_data_missingvalue.csv')
# print(cd)

# column_null = cd.isnull()
# print(column_null.sum())

mean1 = cd['Age'].mean()
cd['Age'] = cd['Age'].fillna(mean1)

mean2 = cd['Annual Income (k$)'].mean()
cd['Annual Income (k$)'] = cd['Annual Income (k$)'].fillna(mean2)

median = cd['Spending Score (1-100)'].median()
cd['Spending Score (1-100)'] = cd['Spending Score (1-100)'].fillna(median)
print(cd)
