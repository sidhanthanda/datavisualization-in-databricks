# Databricks notebook source
import pandas as pd
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic
houses

# COMMAND ----------

titanic.describe()

# COMMAND ----------

houses.describe()

# COMMAND ----------

type(houses.describe())

# COMMAND ----------



# COMMAND ----------


