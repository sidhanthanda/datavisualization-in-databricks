# Databricks notebook source
import pandas as pd

houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
houses
states = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/states.csv")
states

# COMMAND ----------

houses.info()

# COMMAND ----------

states.info()

# COMMAND ----------

houses.dtypes

# COMMAND ----------



# COMMAND ----------


