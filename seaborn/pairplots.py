# Databricks notebook source
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df_house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
df_h25 = df_house.head(30)

# COMMAND ----------

df_house.columns

# COMMAND ----------

sns.pairplot(data=df_house)

# COMMAND ----------


