# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

titanic

# COMMAND ----------

titanic.age.head(10)

# COMMAND ----------

type(titanic.age.head(10))

# COMMAND ----------

netflix.title

# COMMAND ----------

netflix.title.tail(50)

# COMMAND ----------

houses.describe()

# COMMAND ----------

house = houses["price"]
house.describe()

# COMMAND ----------

netflix["rating"]

# COMMAND ----------

netflix["rating"].describe

# COMMAND ----------

netflix.info()

# COMMAND ----------

type(netflix["rating"])

# COMMAND ----------

netflix.release_year.describe()

# COMMAND ----------

titanic.name

# COMMAND ----------


