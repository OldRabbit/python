import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

centroids = kmeans.cluster_centers_

plt.figure(figsize=(10, 7))
scatter = plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=df['Cluster'], cmap='viridis', marker='o', alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, color='red', label='Centroids')
plt.title("K-means Clustering Results")
plt.xlabel("Перша компонента (скейловані дані)")
plt.ylabel("Друга компонента (скейловані дані)")
plt.legend()
plt.colorbar(scatter, label='Cluster')
plt.show()

cluster_means = df.groupby('Cluster').mean()
print("Середні значення показників для кожного кластера:")
print(cluster_means)

for cluster in range(optimal_k):
    print(f"\nКластер {cluster}:")
    cluster_data = cluster_means.loc[cluster]
    
    if cluster_data['Age'] < 30 and cluster_data['Spending Score (1-100)'] > 70:
        print("Характеристики: Молоді клієнти з високими витратами. Рекомендації: Пропонуйте знижки на молодіжні товари та програми лояльності.")
    elif cluster_data['Age'] > 40 and cluster_data['Spending Score (1-100)'] < 40:
        print("Характеристики: Клієнти старшого віку з низькими витратами. Рекомендації: Спеціальні пропозиції на товари для старшого покоління або товари з низькими цінами.")
    elif cluster_data['Annual Income (k$)'] > 60 and cluster_data['Spending Score (1-100)'] > 60:
        print("Характеристики: Клієнти з високим доходом і високими витратами. Рекомендації: Програми преміум-членства та ексклюзивні послуги.")
    else:
        print("Характеристики: Клієнти із середніми значеннями віку, доходу та витрат. Рекомендації: Універсальні пропозиції з акцентом на якість і доступність.")
