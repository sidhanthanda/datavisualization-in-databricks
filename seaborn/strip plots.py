# Databricks notebook source
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

# COMMAND ----------

sns.stripplot(x="price", y="bedrooms", data=house)

# COMMAND ----------

thing = house.head(20)

# COMMAND ----------

sns.stripplot(x="price", y="bedrooms", data=thing, jitter=10)

# COMMAND ----------

sns.stripplot(x="price", y="bedrooms", data=thing, jitter=10, linewidth=0.5)

# COMMAND ----------

sns.stripplot(x="price", y="bedrooms", data=house, hue="waterfront", linewidth=0.5)

# COMMAND ----------

sns.stripplot(x="price", y="bedrooms", data=thing, hue="waterfront", linewidth=0.5, dodge=True)

# COMMAND ----------


