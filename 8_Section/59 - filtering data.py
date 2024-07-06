# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic
house

# COMMAND ----------

titanic.iloc[17:20]

# COMMAND ----------

titanic.sex
titanic.sex == 'female'

# COMMAND ----------

titanic[titanic.sex == 'female']

# COMMAND ----------

titanic

# COMMAND ----------

titanic[titanic["survived"] == 0]


# COMMAND ----------


