import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))

inertia = []
silhouette_scores = []
cluster_range = range(2, 11)

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)  
    silhouette_avg = silhouette_score(scaled_data, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)  

plt.figure(figsize=(10, 5))
plt.plot(cluster_range, inertia, 'bo-', color='blue')
plt.xlabel("Кількість кластерів")
plt.ylabel("Інерція")
plt.title("Метод ліктя: Залежність інерції від кількості кластерів")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(cluster_range, silhouette_scores, 'bo-', color='green')
plt.xlabel("Кількість кластерів")
plt.ylabel("Коефіцієнт силуету")
plt.title("Коефіцієнт силуету для різної кількості кластерів")
plt.show()

optimal_k = cluster_range[silhouette_scores.index(max(silhouette_scores))]
print(f"Оптимальна кількість кластерів за коефіцієнтом силуету: {optimal_k}")
