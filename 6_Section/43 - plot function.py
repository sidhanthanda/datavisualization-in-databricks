# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

netflix

# COMMAND ----------

houses.bedrooms.plot()

# COMMAND ----------

houses.bedrooms.value_counts().plot()

# COMMAND ----------

houses.bedrooms.value_counts().plot(kind = "bar")

# COMMAND ----------

houses.bedrooms.value_counts().plot(kind = "pie")

# COMMAND ----------

titanic.survived

# COMMAND ----------

titanic.survived.value_counts()

# COMMAND ----------

titanic.survived.value_counts().plot(kind = "pie")

# COMMAND ----------

titanic.sex.value_counts().plot(kind = "pie")

# COMMAND ----------

houses.plot()

# COMMAND ----------

houses[["bedrooms", "bathrooms"]].plot()

# COMMAND ----------

df = houses[["bedrooms", "bathrooms"]]
df.plot(x="bedrooms", y= "bathrooms", kind="scatter")

# COMMAND ----------

netflix.rating.value_counts()

# COMMAND ----------

netflix.rating.value_counts().head(10).plot(kind="bar")

# COMMAND ----------


