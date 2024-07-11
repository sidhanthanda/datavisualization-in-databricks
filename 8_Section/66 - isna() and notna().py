# Databricks notebook source
import pandas as pd

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic
house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix

# COMMAND ----------

netflix.info()

# COMMAND ----------

netflix[netflix.director.isna()]

# COMMAND ----------

netflix[netflix["director"].isna() & netflix["cast"].isna()]

# COMMAND ----------

netflix[netflix["director"].notna() & netflix["cast"].notna()]

# COMMAND ----------

netflix[~(netflix["director"].isna()) & ~(netflix["cast"].isna())]

# COMMAND ----------

netflix.shape

# COMMAND ----------


