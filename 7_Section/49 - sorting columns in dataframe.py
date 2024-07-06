# Databricks notebook source
import pandas as pd
df = wh = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv", index_col = 0)
df

# COMMAND ----------

df.sort_values("Healthy life expectancy")

# COMMAND ----------

df.sort_values("Healthy life expectancy", ascending = False)

# COMMAND ----------

df.sort_values("Healthy life expectancy", ascending = False, inplace = True)
df

# COMMAND ----------


