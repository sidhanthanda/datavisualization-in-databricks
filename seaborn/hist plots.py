# Databricks notebook source
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns

df_house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
df_h25 = df_house.head(25)

# COMMAND ----------

sns.histplot(data=df_h25, x="price")

# COMMAND ----------

#sns.histplot(data=df_house, x="price", binwidth=3)

# COMMAND ----------

sns.histplot(data=df_h25, x="price", bins=30)

# COMMAND ----------

sns.histplot(data=df_h25, x="price", bins=np.arrange(0, 2, 0.2))

# COMMAND ----------

dbutils.library.restartPython()


# COMMAND ----------

sns.histplot(data=df_h25, x="price", kde=True)

# COMMAND ----------

sns.histplot(data=df_house, x="price", hue="waterfront", multiple="stack")

# COMMAND ----------

sns.histplot(data=df_h25, x="price", hue="waterfront", element="step")

# COMMAND ----------

sns.histplot(data=df_h25, x="price", hue="waterfront", element="step", fill=False)

# COMMAND ----------

sns.histplot(data=df_house, x="price", hue="waterfront", multiple="stack", fill=False)

# COMMAND ----------

sns.histplot(data=df_house, x="price", hue="waterfront", element="poly")

# COMMAND ----------

sns.histplot(data=df_house, x="price", shrink=0.85)

# COMMAND ----------

sns.histplot(data=df_house, x="price", stat='count')

# COMMAND ----------


