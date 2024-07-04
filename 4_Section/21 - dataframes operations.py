# Databricks notebook source
import pandas as pd

states = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/states.csv")
states

# COMMAND ----------

houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
houses

# COMMAND ----------

type(houses)

# COMMAND ----------

houses.columns

# COMMAND ----------

states.columns

# COMMAND ----------

len(houses)

# COMMAND ----------

houses.shape

# COMMAND ----------

houses.size

# COMMAND ----------

pd.options.display.min_rows = 15

# COMMAND ----------

houses

# COMMAND ----------

houses.head()

# COMMAND ----------

first5 = houses.head() 
first5

# COMMAND ----------

type(first5)

# COMMAND ----------

houses.head(20)

# COMMAND ----------

houses.head(200)

# COMMAND ----------

houses.tail()

# COMMAND ----------

houses.tail(9)

# COMMAND ----------


