# Databricks notebook source
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns

df_house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
df_h25 = df_house.head(25)

# COMMAND ----------

sns.kdeplot(data=df_h25)

# COMMAND ----------

sns.kdeplot(data=df_h25, bw_adjust=2)

# COMMAND ----------

sns.kdeplot(data=df_h25, bw_adjust=2, log_scale=True)

# COMMAND ----------


