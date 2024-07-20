# Databricks notebook source
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
thing = house.head(20)

# COMMAND ----------

sns.swarmplot(x= "price", y="bedrooms", data=thing, )

# COMMAND ----------

sns.swarmplot(x= "price", y="bedrooms", hue="waterfront", data=thing )

# COMMAND ----------


