# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic.head()



# COMMAND ----------

titanic.columns

# COMMAND ----------

titanic.tail(10)

# COMMAND ----------

titanic.info()

# COMMAND ----------


