# Databricks notebook source
import pandas as pd
import matplotlib.pyplot as plt

# COMMAND ----------

data_dict = {
    "Sales": [10,20,30,40],
    "Profits": [2, 4, 3, 1],
    "Date":["2022-01-01", "2022-02-01", "2022-03-01", "2022-04-01" ]
}
    
df = pd.DataFrame(
    data_dict,
    columns=["Sales", "Profits"],
    index = data_dict["Date"]
)

df

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(df)
ax.set_title("Product Sales and Profits")

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(df.index, df["Sales"])
ax.plot(df.index, df["Profits"], ls="--")
ax.set_title("Product Sales and Profits")

# COMMAND ----------


