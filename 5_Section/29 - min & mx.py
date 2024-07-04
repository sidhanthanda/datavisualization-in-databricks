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

houses = w.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")

names = ['sumlev', 'region', 'division', 'state', 'census2010pop', 'estimatesbase2010', 'popstimate2010', 'popestimate2011', 'popestimate2012', 'popestimate2013', 'popestimate2014', 'popestimate2015', 'popestimate2016', 'popestimate2017', 'popestimate2018', 'popestimate2019' , 'popestimate042020', 'popestimate2020']
pop = w.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/nst_est2020.csv", names=names, header=0)
pop

# COMMAND ----------

pop.shape

# COMMAND ----------

pop.head(57)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


