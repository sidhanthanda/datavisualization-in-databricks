# Databricks notebook source
import pandas as pd

df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
df2 = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")


df

# COMMAND ----------

df.sort_index()

# COMMAND ----------

df.sort_index(ascending=False)

# COMMAND ----------

df2.sort_index(ascending = False)

# COMMAND ----------


