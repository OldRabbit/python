import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')

missing_values = df.isnull().sum()
print("Кількість пропущених значень у кожному стовпці:")
print(missing_values)

df.hist(bins=15, figsize=(15, 10))
plt.suptitle("Гістограми розподілу для кожної змінної")
plt.show()

stats = df.describe()
print("Основні статистичні показники для кожної змінної:")
print(stats)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))  # Стандартизуємо тільки числові змінні
scaled_df = pd.DataFrame(scaled_data, columns=df.select_dtypes(include=['float64', 'int64']).columns)

print("Стандартизовані дані (приклад):")
print(scaled_df.head())
