# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

netflix

# COMMAND ----------

hd = houses["bedrooms"]
hd.value_counts()

# COMMAND ----------

titanic.sex.value_counts()

# COMMAND ----------

netflix.director.value_counts()

# COMMAND ----------

netflix.director.value_counts().head()

# COMMAND ----------

netflix.director.value_counts(ascending=True).head()

# COMMAND ----------

netflix.director.value_counts(ascending=True)

# COMMAND ----------

netflix.director.value_counts(ascending=False)

# COMMAND ----------

houses.floors.value_counts()

# COMMAND ----------

houses

# COMMAND ----------

houses[["bedrooms", "bathrooms"]]

# COMMAND ----------

houses[["bedrooms", "bathrooms"]].value_counts()

# COMMAND ----------


