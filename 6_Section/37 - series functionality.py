# Databricks notebook source
import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")

titanic
houses


# COMMAND ----------

pname = titanic.name
type(pname)

# COMMAND ----------

hm = houses.mean()
hm

# COMMAND ----------

type(hm)

# COMMAND ----------


houses.price.sum(numeric_only = True)

# COMMAND ----------

houses.price.max()

# COMMAND ----------

houses.price.min()

# COMMAND ----------

pname.shape

# COMMAND ----------

titanic.shape

# COMMAND ----------

pname.values

# COMMAND ----------

pname.index

# COMMAND ----------

mins = houses.min(numeric_only=True)
mins.values

# COMMAND ----------

mins.index

# COMMAND ----------



# COMMAND ----------


