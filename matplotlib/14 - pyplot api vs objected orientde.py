# Databricks notebook source
import pandas as pd
import matplotlib.pyplot as plt

# COMMAND ----------

data = [x * 10 for x in range(10)]
data

# COMMAND ----------

labels = [f'{x}!' for x in range(10)]

labels

# COMMAND ----------

plt.plot(data)
plt.show()

# COMMAND ----------

plt.plot(data)
plt.title("First Title")
plt.show()

# COMMAND ----------

fig = plt.figure()

ax = fig.add_subplot()
ax.plot(data)
ax.set_title("Title")
fig.suptitle("Overall Title")

# COMMAND ----------


