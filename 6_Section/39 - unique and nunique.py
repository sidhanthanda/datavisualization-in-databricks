# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

houses

# COMMAND ----------

houses["bedrooms"].unique()

# COMMAND ----------

netflix.rating.unique()

# COMMAND ----------

netflix.rating

# COMMAND ----------

netflix.rating.nunique()

# COMMAND ----------

houses.head()

# COMMAND ----------

houses.zipcode.unique()

# COMMAND ----------

houses.zipcode.nunique()

# COMMAND ----------

netflix.info()

# COMMAND ----------

netflix.head()

# COMMAND ----------

netflix.rating.nunique()

# COMMAND ----------

netflix.rating.nunique(dropna = False)

# COMMAND ----------

netflix.rating.nunique(dropna = True)

# COMMAND ----------



# COMMAND ----------


