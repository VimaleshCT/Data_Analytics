import pandas as pd
data = pd.read_csv(r"C:\Users\prano\Desktop\study\DS and ML\Data Analytics\Netflix+Dataset.csv")
print(data)


print(data.shape)

#heatmap
import seaborn as sb
import matplotlib.pyplot as plt
sb.heatmap(data.isnull())
plt.show()

#drop duplicate
print(data.drop_duplicates(inplace=True))

#5Gang. what is show id and director
d =data[data['Title'].isin(['5Gang'])]
print(d)

#datatypes
print(data.dtypes)




#all movies released  in 2000
print((data['Category'] == 'Movie') & (data['Year'] ==2000))



#movies and tv show using bargraph
print(data.groupby('Type').Type.count())
sb.countplot((data['Type']))

