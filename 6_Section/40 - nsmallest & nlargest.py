# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

houses

# COMMAND ----------

houses.price.nlargest()

# COMMAND ----------

houses.price.nlargest(9)

# COMMAND ----------

houses.price.nsmallest(10)

# COMMAND ----------

titanic.pclass.nlargest(5)

# COMMAND ----------

titanic.pclass.nlargest(5, keep="all")

# COMMAND ----------

titanic.pclass.nlargest(10)

# COMMAND ----------

houses.nlargest(10, "price")

# COMMAND ----------

houses.nlargest(10, "bedrooms")

# COMMAND ----------

houses.nlargest(10, ["bedrooms", "bathrooms"])

# COMMAND ----------

houses.nlargest(10, ["sqft_lot"])

# COMMAND ----------


