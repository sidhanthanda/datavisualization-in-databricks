# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house

# COMMAND ----------

house["bedrooms"].between(5, 7).value_counts()

# COMMAND ----------

house["bedrooms"].between(5, 7).value_counts()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


