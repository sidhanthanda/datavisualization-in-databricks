# Databricks notebook source
# MAGIC %md
# MAGIC ### Integer index

# COMMAND ----------

import pandas as pd


data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df_int_index = pd.DataFrame(data)
df_int_index.iloc[:,2]


# COMMAND ----------

# MAGIC %md
# MAGIC ### string/label based index

# COMMAND ----------



data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df_label_index = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4'])
df_label_index

df_label_index.loc["row2"]


# COMMAND ----------


