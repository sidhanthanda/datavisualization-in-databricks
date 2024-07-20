# Databricks notebook source
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

# COMMAND ----------

house.columns

# COMMAND ----------

thing = house.head(12)
thingpl

# COMMAND ----------


plt.figure(figsize=(15, 6))


sns.violinplot(x="price", y="bedrooms", data=thing)


plt.show()


# COMMAND ----------


plt.figure(figsize=(15, 6))


sns.violinplot(y="price", data=thing)


plt.show()


# COMMAND ----------



# COMMAND ----------


plt.figure(figsize=(15, 6))


sns.violinplot(y="bedrooms", x="bathrooms", data=house, hue="waterfront", split=True)


plt.show()


# COMMAND ----------

#print(thing['waterfront'].unique())  # This will show all unique values in the 'waterfront' column.
thing.waterfront

# COMMAND ----------


plt.figure(figsize=(15, 6))


sns.violinplot(y="bedrooms", x="bathrooms", data=house, hue="waterfront", split=True, inner='quartile')


plt.show()


# COMMAND ----------


plt.figure(figsize=(15, 6))


sns.violinplot(y="bedrooms", x="bathrooms", data=house, hue="waterfront", split=True, inner='quartile', bw=.2)


plt.show()


# COMMAND ----------


plt.figure(figsize=(15, 6))


sns.violinplot(y="bedrooms", x="bathrooms", data=house, hue="waterfront", split=True, inner='quartile', bw=.2, cut=0)


plt.show()

