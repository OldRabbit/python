import joblib
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target

# Function to calculate adjusted R²
def adjusted_r2(r2, n, k):
    return 1 - ((1 - r2) * (n - 1) / (n - k - 1))

# Step 1: Simple Linear Regression with the most correlated feature
correlation_matrix = df.corr()
most_correlated_feature = correlation_matrix['MedHouseVal'].drop('MedHouseVal').idxmax()

X_simple = df[[most_correlated_feature]]
y = df['MedHouseVal']
X_train_simple, X_test_simple, y_train, y_test = train_test_split(X_simple, y, test_size=0.2, random_state=42)

simple_model = LinearRegression()
simple_model.fit(X_train_simple, y_train)
y_pred_simple = simple_model.predict(X_test_simple)

mse_simple = mean_squared_error(y_test, y_pred_simple)
rmse_simple = np.sqrt(mse_simple)
r2_simple = r2_score(y_test, y_pred_simple)
adj_r2_simple = adjusted_r2(r2_simple, len(y_test), 1)

# Step 2: Multiple Linear Regression with all features
X = df.drop('MedHouseVal', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

multi_model = LinearRegression()
multi_model.fit(X_train_scaled, y_train)
y_pred_multi = multi_model.predict(X_test_scaled)

mse_multi = mean_squared_error(y_test, y_pred_multi)
rmse_multi = np.sqrt(mse_multi)
r2_multi = r2_score(y_test, y_pred_multi)
adj_r2_multi = adjusted_r2(r2_multi, len(y_test), X.shape[1])

# Step 3: Optimized Model with Ridge Regression and selected features
top_features = correlation_matrix['MedHouseVal'].drop('MedHouseVal').nlargest(4).index.tolist()
X_opt = df[top_features]
X_train_opt, X_test_opt, y_train, y_test = train_test_split(X_opt, y, test_size=0.2, random_state=42)
X_train_opt_scaled = scaler.fit_transform(X_train_opt)
X_test_opt_scaled = scaler.transform(X_test_opt)

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_opt_scaled, y_train)
y_pred_opt = ridge_model.predict(X_test_opt_scaled)

mse_opt = mean_squared_error(y_test, y_pred_opt)
rmse_opt = np.sqrt(mse_opt)
r2_opt = r2_score(y_test, y_pred_opt)
adj_r2_opt = adjusted_r2(r2_opt, len(y_test), len(top_features))

# Display metrics for each model
print("\nModel Performance Comparison:")
print(f"Simple Linear Regression - MSE: {mse_simple}, RMSE: {rmse_simple}, R2: {r2_simple}, Adjusted R2: {adj_r2_simple}")
print(f"Multiple Linear Regression - MSE: {mse_multi}, RMSE: {rmse_multi}, R2: {r2_multi}, Adjusted R2: {adj_r2_multi}")
print(f"Optimized Model (Ridge) - MSE: {mse_opt}, RMSE: {rmse_opt}, R2: {r2_opt}, Adjusted R2: {adj_r2_opt}")

# Step 4: Visualization of Predictions vs Actual Values
models = {'Simple Linear Regression': (y_test, y_pred_simple),
          'Multiple Linear Regression': (y_test, y_pred_multi),
          'Optimized Ridge Model': (y_test, y_pred_opt)}

for model_name, (y_true, y_pred) in models.items():
    plt.figure(figsize=(10, 5))
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'k--', lw=2)
    plt.xlabel("Actual Median House Value")
    plt.ylabel("Predicted Median House Value")
    plt.title(f"{model_name} - Predicted vs Actual")
    plt.show()

    # Step 5: Residual Analysis
    residuals = y_true - y_pred
    
    # Residuals vs Predicted Values
    plt.figure(figsize=(10, 5))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel("Predicted Median House Value")
    plt.ylabel("Residuals")
    plt.title(f"{model_name} - Residuals vs Predicted Values")
    plt.show()

    # Distribution of Residuals
    plt.figure(figsize=(10, 5))
    sns.histplot(residuals, kde=True)
    plt.xlabel("Residuals")
    plt.title(f"{model_name} - Distribution of Residuals")
    plt.show()
