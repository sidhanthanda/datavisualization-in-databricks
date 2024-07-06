# Databricks notebook source
import pandas as pd
btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc

#the .set_index() method deosnt work in other cells

# COMMAND ----------

edit = btc.set_index("Date")
edit

# COMMAND ----------

btc.index

# COMMAND ----------

btc.High

# COMMAND ----------

btc.High.plot()

# COMMAND ----------

import pandas as pd
btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc.High.plot

# COMMAND ----------

# MAGIC %md
# MAGIC
