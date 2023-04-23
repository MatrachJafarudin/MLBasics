import pandas
from sklearn import linear_model

df = pandas.read_csv('co2_prediction.csv')

# independent values
X = df[['Weight', 'Volume']]
# dependent values
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X.values, y)

predicted_co2 = regr.predict([[2300, 1300]])
print('Prediction from csv ==============================')
print(predicted_co2)

# check the coefficiend and test what would happen if we increase the volume by 1000kg
# print(regr.coef_)
print('Predict with a volume increased by 1000kg ==============================')
new_predicted_co2 = regr.predict([[3300, 1300]])
print(new_predicted_co2)