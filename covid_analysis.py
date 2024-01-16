import pandas as pd
data = pd.read_csv(r"D:/Python/Covid_19_data.csv")
print(data)

#remove data that contains missing values only
print(data.isnull().sum())

# import seaborn as sb
# import matplotlib.pyplot as plt
# sb.heatmap(data.isnull())
# plt.show()

#no .of confirmed , deaths amd recovered case in each region
print(data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False))

#remove all records where confirmed is < 10
data = data[~(data.Confirmed<10)]
print(data)

#max confirmed case among region
print(data.groupby('Region').Confirmed.sum().sort_values(ascending=False))


#min deaths among region
print(data.groupby('Region').Deaths.sum().sort_values(ascending=True))

#confirmed ,deaths&recovered case in india till 29apr 2020
print(data[data.Region == ' India'])