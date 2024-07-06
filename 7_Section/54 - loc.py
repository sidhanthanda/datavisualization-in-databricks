# Databricks notebook source
import pandas as pd

df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
df

# COMMAND ----------

df.index()

# COMMAND ----------



# COMMAND ----------


df.iloc[144:145]


# COMMAND ----------



# COMMAND ----------


