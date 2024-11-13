import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target

correlation_matrix = df.corr()
most_correlated_feature = correlation_matrix['MedHouseVal'].drop('MedHouseVal').idxmax()
print(f"Most correlated feature with target: {most_correlated_feature}")

X_simple = df[[most_correlated_feature]]
y = df['MedHouseVal']

X_train_simple, X_test_simple, y_train, y_test = train_test_split(X_simple, y, test_size=0.2, random_state=42)

simple_model = LinearRegression()
simple_model.fit(X_train_simple, y_train)

y_pred_simple = simple_model.predict(X_test_simple)
mse_simple = mean_squared_error(y_test, y_pred_simple)
r2_simple = r2_score(y_test, y_pred_simple)

print(f"Simple Linear Regression - MSE: {mse_simple}, R2: {r2_simple}")

plt.figure(figsize=(8, 6))
plt.scatter(X_test_simple, y_test, color='blue', label='Actual')
plt.plot(X_test_simple, y_pred_simple, color='red', label='Predicted')
plt.xlabel(most_correlated_feature)
plt.ylabel('Median House Value')
plt.title('Simple Linear Regression Results')
plt.legend()
plt.show()

X = df.drop('MedHouseVal', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, 'scaler.joblib')

multi_model = LinearRegression()
multi_model.fit(X_train_scaled, y_train)

y_pred_multi = multi_model.predict(X_test_scaled)
mse_multi = mean_squared_error(y_test, y_pred_multi)
r2_multi = r2_score(y_test, y_pred_multi)

print(f"Multiple Linear Regression - MSE: {mse_multi}, R2: {r2_multi}")

coefficients = pd.DataFrame(multi_model.coef_, X.columns, columns=['Coefficient'])
print("\nMultiple Linear Regression Coefficients:\n", coefficients)

top_features = correlation_matrix['MedHouseVal'].drop('MedHouseVal').nlargest(4).index.tolist()
print(f"Selected features for optimized model: {top_features}")

X_opt = df[top_features]

X_train_opt, X_test_opt, y_train, y_test = train_test_split(X_opt, y, test_size=0.2, random_state=42)
X_train_opt_scaled = scaler.fit_transform(X_train_opt)
X_test_opt_scaled = scaler.transform(X_test_opt)

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_opt_scaled, y_train)

y_pred_opt = ridge_model.predict(X_test_opt_scaled)
mse_opt = mean_squared_error(y_test, y_pred_opt)
r2_opt = r2_score(y_test, y_pred_opt)

print(f"Optimized Model (Ridge Regression) - MSE: {mse_opt}, R2: {r2_opt}")
print("\nModel Comparison:")
print(f"Simple Linear Regression - MSE: {mse_simple}, R2: {r2_simple}")
print(f"Multiple Linear Regression - MSE: {mse_multi}, R2: {r2_multi}")
print(f"Optimized Model (Ridge) - MSE: {mse_opt}, R2: {r2_opt}")
