# Databricks notebook source
import pandas as pd

#dbfs path to the catalog in databricks
path= "/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv"

# read using the variable
housedata = pd.read_csv(path)
housedata

# COMMAND ----------

housedata.min()

# COMMAND ----------

housedata.max()

# COMMAND ----------

housedata.sum()

# COMMAND ----------

housedata.sum(numeric_only = True)

# COMMAND ----------

1.167293e+10

# COMMAND ----------

titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic

# COMMAND ----------

titanic.sum(numeric_only = True)

# COMMAND ----------




names = ['sumlev', 'region', 'division', 'state', 'name', 'census2010pop', 'estimatesbase2010', 'popestimate2010', 'popestimate2011', 'popestimate2012','popestimate2013', 'popestimate2014', 'popestimate2015', 'popestimate2016', 'popestimate2017', 'popestimate2018', 'popestimate2019', 'popestimate042020', 'popestimate2020']


data_frame = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/nst_est2020.csv", names =names, header = 0)
data_frame


# COMMAND ----------

data_frame.tail(52).head(51).sum(numeric_only = True)

# COMMAND ----------

titanic.count()

# COMMAND ----------

housedata.mean()

# COMMAND ----------

titanic.mean()

# COMMAND ----------

titanic.mode()

# COMMAND ----------

titanic.mode(numeric_only = True)

# COMMAND ----------

titanic.describe()

# COMMAND ----------

housedata.describe()

# COMMAND ----------

titanic.describe(include=["O",  "int64"])

# COMMAND ----------


