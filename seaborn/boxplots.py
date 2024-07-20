# Databricks notebook source
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

# COMMAND ----------

house.columns

# COMMAND ----------

sns.boxplot(x="price",y="bedrooms", data=house)

# COMMAND ----------

sns.boxplot(x="price",y="bedrooms", data=house, hue="waterfront")

# COMMAND ----------

plt.figure(figsize=(26, 19))

sns.boxplot(x="price",y="bedrooms", data=house, hue="waterfront", showmeans= "True")

# COMMAND ----------

sns.boxplot(x="price",y="bedrooms", data=house, hue="waterfront", showmeans= "True", meanprops = {"marker": "o", "markerfacecolor": "white", "markersize": "5", "markeredgecolor": "black"})

# COMMAND ----------

sns.boxplot(y="price",x="bedrooms", data=house, hue="waterfront", showmeans= "True", meanprops = {"marker": "o", "markerfacecolor": "white", "markersize": "5", "markeredgecolor": "black"})

# COMMAND ----------


