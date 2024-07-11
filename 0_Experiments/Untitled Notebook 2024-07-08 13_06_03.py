# Databricks notebook source
import pandas as pd

df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")


# COMMAND ----------

type(df)

# COMMAND ----------

df["name"]

# COMMAND ----------

type(df.name)

# COMMAND ----------


