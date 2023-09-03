import pandas as pd
data = pd.read_csv(r"C:\Users\prano\Desktop\study\DS and ML\Project+1+-+Weather+Dataset.csv")
print(data)
# 
# print(data.head(2))
# 
# print(data.shape)
# 
# print(data.index)
# 
# print(data.columns)
# 
# print(data.dtypes)
# 
# print(data['Weather'].unique())
# 
# print(data['Weather'].nunique())
# 
# print(data.count())
# 
# 
# print(data['Weather'].value_counts())
# 
# print(data.info())

# to find all unique values of "wind speed"
print(data['Wind Speed_km/h'].unique())

#to find no.of times when"weather is exactly clear"
print(data[data.Weather == 'Clear'])
 
#find no.of times exactly wind speed 4km/h
print(data[data['Wind Speed_km/h'] == 4])


#find null values in data
print(data.isnull().sum())

#rename column name "weather" to "weather cond"
print(data.rename(columns = {'Weather' : 'Weather Condition'}, ))

#what is mean visibility
print(data.Visibility_km.mean())

#what is standard deviation of "pressure"
print(data.Press_kPa.std())

#variance of"relative humidity"
print(data['Rel Hum_%'].var())

#all instance when snow recorded
print(data[data['Weather'].str.contains('Snow')])

#find instance when visibility is 25 and wind speed >24
print(data[(data['Wind Speed_km/h'] >24)& (data['Visibility_km'] == 25)])



#all records where fog 
print(data[data[' Weather'] == 'Fog'])