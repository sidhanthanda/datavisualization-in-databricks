# Databricks notebook source
import pandas as pd
df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")

df

# COMMAND ----------

df.sort_values("name").plot()
#databricks orders it as ABC....XYZ....abc...xyz

# COMMAND ----------

df.sort_values("name", key=lambda col: col.str.lower())


# COMMAND ----------



# COMMAND ----------


