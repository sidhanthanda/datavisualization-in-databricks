# Databricks notebook source
import pandas as pd
df1 = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
df2 = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv", index_col = 0)

df1

# COMMAND ----------

df1.sort_values("price", ascending= False)

# COMMAND ----------

df1.sort_values("bedrooms", ascending= False)

# COMMAND ----------

df1.sort_values(["bedrooms", "bathrooms"], ascending= False)

# COMMAND ----------


