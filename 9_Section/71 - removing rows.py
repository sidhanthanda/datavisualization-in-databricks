# Databricks notebook source
import pandas as pd
country= pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
country


country.set_index("Country name", inplace=True)
country

btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc

# COMMAND ----------

country.drop(labels="Denmark", axis=0)


# COMMAND ----------

country

# COMMAND ----------

country.drop(["Denmark", "Iceland", "Finland"])

# COMMAND ----------

btc.sort_index()

# COMMAND ----------

btc.sort_index(ascending=False)

# COMMAND ----------

btc.sort_index(ascending=False, inplace=True)
btc.drop(2990)

# COMMAND ----------

country

# COMMAND ----------

country.drop(country.index[0:3])

# COMMAND ----------

country.drop(country.index[1:])

# COMMAND ----------

country.drop(country.index[10:])

# COMMAND ----------


