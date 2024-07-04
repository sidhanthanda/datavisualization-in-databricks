# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|", index_col=0)
netflix

# COMMAND ----------

houses.describe()

# COMMAND ----------

type(houses.floors)

# COMMAND ----------

houses/

# COMMAND ----------

houses["price"].describe()

# COMMAND ----------

netflix.rating.descrube()

# COMMAND ----------

netflix.rating.describe()

# COMMAND ----------

netflix.dtypes

# COMMAND ----------

type(netflix.dtypes)

# COMMAND ----------

netflix.date_added.describe()

# COMMAND ----------

titanic.name.dtype

# COMMAND ----------

houses[bedrooms].unqiue()

# COMMAND ----------


