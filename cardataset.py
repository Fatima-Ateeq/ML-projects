import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

"""
Load the dataset
"""
df = pd.read_csv("cardekho_dataset.csv")



"""
Understand the dataset
"""
print(df['model'].unique())
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.isnull().sum())
print(df['selling_price'].value_counts())
colum = df.columns
for col in df[colum]:
    print(df[col].value_counts())
    print("-"*50)

for colu in df[colum]:
    print(df[col].isnull().sum())
    print("_"*40)

print(df.duplicated().sum())

num_col = df.select_dtypes(include="number").columns
obj_col = df.select_dtypes(include="object").columns
print(num_col)
print(obj_col)



"""
EDA (Exploratory Data Analysis)
"""

print(df.columns.tolist())
print(df["selling_price"].describe())
plt.hist(df['selling_price'], bins=50)
plt.xlabel("selling price")
plt.ylabel("number of cars")
plt.title("Selling Price Distribution")
plt.ticklabel_format(style='plain', axis='x')
plt.show()


plt.scatter(df['vehicle_age'], df['selling_price'])
plt.xlabel("Vehicle Age")
plt.ylabel("Selling Price")
plt.title("Vehicle Age vs Selling Price")
plt.show()


"""
Data Preprocessing
"""

df.drop('Unnamed: 0', axis=1, inplace= True)
print("after drop unamed column\n",df.columns)
print(df['engine'].isnull().sum())


print(df[['car_name', 'brand', 'model']].head(20))
#drop car_name column because it is a combination of model and brand 
df.drop('car_name', axis=1, inplace= True)
print(df.columns)




"""
Encoding categorical columns
"""
#use one hot encoding (0,1)
cate_col = df.select_dtypes(include='object').columns.tolist()
print(cate_col)
print("type",type(cate_col))
df = pd.get_dummies(df, columns=cate_col, dtype=int)
print(df.head())

print(df)




"""
Feature Engineering
"""
X = df.drop('selling_price', axis =1)
y = df['selling_price']
print("simple X: \n",X)
print("simple y: \n",y)




from sklearn.model_selection import train_test_split
"""
Splitting the data in train and test data
"""
train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)



"""Feature scalling"""
from sklearn.preprocessing import StandardScaler
scalerr = StandardScaler()
X_train_scaled = scalerr.fit_transform(X_train)
x_test_scaled = scalerr.transform(X_test)
print(x_test_scaled[:5])



"""
Model Training 🤖
"""
"""
Because your target is:

y = selling_price

which is continuous, this is a Regression problem.

So you need regression models, not classification models.

Good models to start with:

1. Linear Regression ← start here
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor"""


"""
1.
"""

# LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# PREDICTION
y_predict = model.predict(x_test_scaled)
print("Y_PREDCITON\n",y_predict[:10])
print("y_test", y_test[:10])


#EVALUATION

# For your car selling-price prediction, you have a regression problem, so we normally don't use accuracy_score like we did for churn classification.

# Instead, use R² score as a main measure of how well the model fits the target:
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict)
print("R2: ", r2)
print("R2 percentage: ", r2*100,"%")



from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

mae = mean_absolute_error(y_test, y_predict)
# For MAE(mean absolute error):

# MAE ↓ LOWER = BETTER ✅
# MAE ↑ HIGHER = WORSE ❌

rmse = np.sqrt(mean_squared_error(y_test, y_predict))
#RMSE: large errors are having a significant effect, since RMSE is much higher than MAE.

print("mae: ", mae)
print("rmse: ", rmse)


"""
Remember:

Classification → Accuracy, Precision, Recall, F1
Regression → MAE, RMSE, R²
"""




"""
2.
"""
#DECISION TREE REGRESSOR
from sklearn.tree import DecisionTreeRegressor
model_dtr = DecisionTreeRegressor(random_state=42)
model_dtr.fit(X_train, y_train)

#PREDICTION
y_pred = model_dtr.predict(X_test)

#EVALUATION
r2_dtr = r2_score(y_test,y_pred)
print("\nr2_dtr: ", r2_dtr)
print("r2_dtr percentage: ", r2_dtr*100,"%")

mae_dtr = mean_absolute_error(y_test,y_pred)
print("mae_dtr: ", mae_dtr)
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print("rmse: ", rmse)



"""
3.
"""
print("Random Forest:\n")
#RANDOM FOREST REGRESSOR
from sklearn.ensemble import RandomForestRegressor
model_randomfr = RandomForestRegressor()
model_randomfr.fit(X_train, y_train)


#PREDICTION
y_predd = model_randomfr.predict(X_test)


#EVALUATION
r2_randomfr = r2_score(y_test, y_predd)
print("\nR2_Score RandomFR: ",r2_randomfr)
print("R2_sore RandomeFr %: ", r2_randomfr*100,"%")

mae_random = mean_absolute_error(y_test,y_predd)
print("mae_random: ", mae_random)
rmse_random = np.sqrt(mean_squared_error(y_test,y_predd))
print("rmse_random: ", rmse_random)






print("\n\n")

from sklearn.model_selection import GridSearchCV

model_rf = RandomForestRegressor(random_state=42)
param_grid = {
    'n_estimators': [100],
    'max_depth': [10, 20],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(
    estimator=model_rf,
    param_grid=param_grid,
    cv=3,
    scoring='r2',
    n_jobs=-1
)
# param_grid = {
#     'n_estimators': [100, 200],
#     'max_depth': [10, 20, None],
#     'min_samples_split': [2, 5],
#     'min_samples_leaf': [1, 2]
# }

# grid_search = GridSearchCV(
#     estimator=model_rf,
#     param_grid=param_grid,
#     cv=5,
#     scoring='r2',
#     n_jobs=-1
# )

grid_search.fit(X_train, y_train)
print("Best Parameters:")
print(grid_search.best_params_)
best_model = grid_search.best_estimator_
y_pred_tuned = best_model.predict(X_test)
r2_tuned = r2_score(y_test, y_pred_tuned)
print("Tuned Random Forest")
print("R2:", r2_tuned)
mae_tuned = mean_absolute_error(y_test, y_pred_tuned)
rmse_tuned = np.sqrt(mean_squared_error(y_test, y_pred_tuned))

print("Tuned Random Forest")
print("R2:", r2_tuned)
print("R2 Percentage:", r2_tuned * 100, "%")
print("MAE:", mae_tuned)
print("RMSE:", rmse_tuned)





"""
4.
"""
#GRADIENT BOASTING
from sklearn.ensemble import GradientBoostingRegressor
model_Gradbr = GradientBoostingRegressor()
model_Gradbr.fit(X_train,y_train)

#PREDICTION
y_preddi = model_Gradbr.predict(X_test)


#EVALUATION
r2_Gradient = r2_score(y_test, y_preddi)
print("\nR2_score GradientBoostingRegressor: ", r2_Gradient)
print("R2_score GradientBoostRegressor: ",r2_Gradient*100,"%")

mae_grad = mean_absolute_error(y_test, y_preddi)
rmsr_grad = np.sqrt(mean_squared_error(y_test, y_preddi))
print("mae grad: ", mae_grad)
print("rmse_grad:: ",rmsr_grad)

print(X_train.columns)





"""
we have made 4 models 
when we have check prediction and Evaluation then found Random Forest best model
"""
importance = model_randomfr.feature_importances_
feature_importance = pd.DataFrame({
    "Feature" : X_train.columns,
    "importance":importance
})
feature_importance = feature_importance.sort_values(
    by = "importance",
    ascending= False
)
print(feature_importance)
#✅ "max_power is the most important feature according to the Random Forest model, with a feature importance of approximately 64.67%."





"""
save the model
"""
# best model is the original Random Forest, because it achieved:

# R²   = 92.67%
# MAE  = 103,250
# RMSE = 232,700


import joblib
joblib.dump(model_randomfr, "car_price_model.pkl")
joblib.dump(X_train.columns.tolist(), "car_columns.pkl")






model = joblib.load("car_price_model.pkl")
m_columns = joblib.load("car_columns.pkl")

print(m_columns)

new_car = {
    'vehicle_age': 3,
    'km_driven': 30000,
    'mileage': 20.5,
    'engine': 1498,
    'max_power': 110,
    'seats': 5,
    'brand': 'Maruti',
    'model': 'Swift',
    'seller_type': 'Individual',
    'fuel_type': 'Petrol',
    'transmission_type': 'Manual'
}
new_car_df = pd.DataFrame([new_car])
#converts categorical values into numbers.
new_car_df = pd.get_dummies(new_car_df, dtype=int)

new_car_df = new_car_df.reindex(columns=X_train.columns, fill_value=0)
prediction = model_randomfr.predict(new_car_df)

print("Predicted Selling Price:", prediction[0])