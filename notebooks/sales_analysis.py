# E-Commerce Sales Analysis
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

print(df.describe(include="all"))
print("Total sales:", df["sales"].sum())
print("Total profit:", df["profit"].sum())
print("Orders:", df["order_id"].nunique())
print("Customers:", df["customer_id"].nunique())
print("AOV:", df["sales"].sum()/df["order_id"].nunique())

monthly = df.groupby("month", as_index=False)["sales"].sum()
category = df.groupby("category", as_index=False)["sales"].sum().sort_values("sales", ascending=False)
product = df.groupby("product", as_index=False)["sales"].sum().sort_values("sales", ascending=False).head(10)
region = df.groupby("region", as_index=False)["sales"].sum().sort_values("sales", ascending=False)

monthly.plot(x="month", y="sales", kind="line", figsize=(10,5), title="Monthly Sales")
plt.xticks(rotation=45); plt.tight_layout(); plt.show()

category.plot(x="category", y="sales", kind="bar", figsize=(9,5), title="Sales by Category")
plt.xticks(rotation=30); plt.tight_layout(); plt.show()

product.plot(x="product", y="sales", kind="barh", figsize=(9,5), title="Top 10 Products")
plt.tight_layout(); plt.show()

region.plot(x="region", y="sales", kind="bar", figsize=(8,5), title="Sales by Region")
plt.tight_layout(); plt.show()
