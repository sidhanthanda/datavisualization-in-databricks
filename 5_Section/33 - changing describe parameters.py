# Databricks notebook source
import pandas as pd
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep = "|")
titanic
houses
netflix 

# COMMAND ----------

titanic.describe()

# COMMAND ----------

houses.describe()

# COMMAND ----------

type(houses.describe())

# COMMAND ----------

titanic.describe(include=["object"])

# COMMAND ----------

titanic.describe(include=["O"])
#does the same thing as the previous cell

# COMMAND ----------

titanic.describe(include=["object", "int64"])

# COMMAND ----------

netflix.describe(include=["O"])

# COMMAND ----------


