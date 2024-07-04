# Databricks notebook source
import pandas as w
houses = w.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
houses

# COMMAND ----------

houses.min()

# COMMAND ----------

houses.max()

# COMMAND ----------

type(houses.max())

# COMMAND ----------

houses.sum()

# COMMAND ----------

"h" + "3110"

# COMMAND ----------

houses.sum(numeric_only = True)

# COMMAND ----------

titanic = w.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic.head()

# COMMAND ----------

titanic.sum()

# COMMAND ----------

titanic.sum(numeric_only = True)

# COMMAND ----------

names = ['sumlev', 'region', 'division', 'state', 'census2010pop', 'estimatesbase2010', 'popstimate2010', 'popestimate2011', 'popestimate2012', 'popestimate2013', 'popestimate2014', 'popestimate2015', 'popestimate2016', 'popestimate2017', 'popestimate2018', 'popestimate2019' , 'popestimate042020', 'popestimate2020']
pop = w.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/nst_est2020.csv", names=names, header=0)
pop

# COMMAND ----------

pop.tail(52).head(51).sum(numeric_only = True)

# COMMAND ----------

titanic.count()

# COMMAND ----------

netflix = w.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep= "|", index_col = 0)
netflix.head()

# COMMAND ----------

netflix.count()

# COMMAND ----------


