# Databricks notebook source
import pandas as pd

pop = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/nst_est2020.csv")
pop.columns

# COMMAND ----------

names = ['sumlev', 'region', 'division', 'state', 'census2010pop', 'estimatesbase2010', 'popstimate2010', 'popestimate2011', 'popestimate2012', 'popestimate2013', 'popestimate2014', 'popestimate2015', 'popestimate2016', 'popestimate2017', 'popestimate2018', 'popestimate2019' , 'popestimate042020', 'popestimate2020']
pop = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/nst_est2020.csv", names=names, header=0)
pop

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


