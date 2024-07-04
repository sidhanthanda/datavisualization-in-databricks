# Databricks notebook source
import pandas as pd
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv")
netflix

# COMMAND ----------

netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep= "|")
netflix

# COMMAND ----------

netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep= "|", index_col = 0)
netflix

# COMMAND ----------

netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep= "|", index_col = 3)
netflix

# COMMAND ----------

netflix.info()

# COMMAND ----------

netflix.head()

# COMMAND ----------


