# 🧩 K-Means Customer Clustering

A beginner-friendly ML project that groups customers into segments based on **Age** and **Spending** using the **K-Means clustering algorithm** (unsupervised learning).

---

## 📌 What This Project Does

- 📊 Takes a small dataset of customers (`Age`, `Spending`)
- 🤖 Trains a `KMeans` model to group customers into **3 clusters**
- 🏷️ Assigns each customer a `Cluster` label
- 📈 Plots a scatter chart (Age vs Spending), color-coded by cluster
- 💾 Saves the plot as `customer_clustering.png`

---

## 🧠 Why K-Means?

K-Means is an **unsupervised** algorithm — there are no "correct answers" (labels) given beforehand. It looks at how data points are spread out and groups similar ones together based on distance.

Here, customers with similar **age + spending patterns** end up in the same cluster — useful for things like:
- 🎯 Targeted marketing
- 🛍️ Customer segmentation
- 💰 Identifying high-spender vs low-spender groups

---

## 🗂️ Dataset

A small hardcoded dataset of 10 customers:

| Age | Spending |
|-----|----------|
| 20  | 20       |
| 22  | 25       |
| 25  | 30       |
| ... | ...      |
| 50  | 90       |

---

## ⚙️ Tech Stack

- 🐍 Python
- 🐼 pandas — data handling
- 📉 matplotlib — visualization
- 🧪 scikit-learn — KMeans model

---

## 🚀 How to Run

1. Clone this repo
   ```bash
   git clone https://github.com/vighneshgaikwad59-web/kmeans-customer-clustering.git
   cd kmeans-customer-clustering
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script
   ```bash
   python kmeans_clustering.py
   ```

4. Check the output
   - Cluster assignments print in the terminal 🖥️
   - A scatter plot pops up and saves as `customer_clustering.png` 🖼️

---

## 📸 Sample Output

The scatter plot shows customers grouped into 3 color-coded clusters based on Age and Spending — younger/low-spenders, mid-range customers, and older/high-spenders typically separate out clearly.

---

## 🔧 Things You Can Tweak

- Change `n_clusters=3` → try `2`, `4`, or more to see different groupings
- Change `random_state` → different starting points (results may shift slightly)
- Add more features (e.g., `Income`) to the dataset for richer clustering

---

## ✨ Author

**Vighnesh Gaikwad**
🔗 [GitHub](https://github.com/vighneshgaikwad59-web)
