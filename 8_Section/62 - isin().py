# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix

# COMMAND ----------

netflix.shape

# COMMAND ----------

countries = ["India", "Japan", "South Korea"]
netflix[netflix["country"].isin(countries)]

# COMMAND ----------

countries = ["India", "Japan", "South Korea"]
netflix[netflix["country"].isin(countries)].country.value_counts()

# COMMAND ----------

ra = ["TV-MA", "R"]
netflix[netflix["rating"].isin(ra)]

# COMMAND ----------


