import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "Age": [20, 22, 25, 27, 30, 35, 40, 42, 45, 50],
    "Spending": [20, 25, 30, 35, 40, 60, 70, 75, 80, 90]
}
df = pd.DataFrame(data)

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42)
#random_state=42 → fixes the random starting point
#n_clusters=2 for 2 clusters, n_clusters=3 for 3 clusters, etc.

model.fit(df)

df["Cluster"] = model.labels_
#model.labels_ = tells us which cluster each data point belongs to.

print("----------Cluster Centers:-----------------")
print(df)

# Visualize clusters
plt.scatter(
    df["Age"],
    df["Spending"],
    c=df["Cluster"]
)

plt.xlabel("Age")
plt.grid(True)
plt.ylabel("Spending")
plt.title("K-Means Customer Clustering")
plt.savefig("customer_clustering.png")
plt.show()