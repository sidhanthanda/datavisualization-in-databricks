# Databricks notebook source
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# COMMAND ----------

house = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
house.shape
house.columns

# COMMAND ----------

house.waterfront

# COMMAND ----------

import seaborn as sns
import matplotlib.pyplot as plt

# Using histplot to create a histogram
sns.countplot(data=house, x="price")  # You can adjust the number of bins based on your specific data range
plt.show()


# COMMAND ----------



# COMMAND ----------

sns.countplot(x= "bedrooms", data = house)

# COMMAND ----------

plt.figure(figsize=(15, 5))

sns.countplot(y  = "bedrooms", data = house)

# COMMAND ----------

plt.figure(figsize=(20, 6))

sns.scatterplot(y= "price", x = "bedrooms", data = house)

# COMMAND ----------

plt.figure(figsize=(20, 6))

sns.scatterplot(y= "price", x = "bedrooms", data = house, hue = "waterfront", palette='muted')

# COMMAND ----------

house.price.min()

# COMMAND ----------

plt.figure(figsize=(20, 6))

sns.countplot(x = "price", data=house
                ,facecolor = (0, 0, 0, 0)
                ,linewidth=5 
                ,edgecolor=sns.color_palette('dark', 3)
                )

# COMMAND ----------

# plt.figure(figsize=(20, 6))

# sns.barplot(y= "price", x = "bedrooms", data = house, hue = "waterfront", palette='muted')


# COMMAND ----------

sns.get_dataset_names()
si = sns.load_dataset('seaice')
si.max()

# COMMAND ----------

si.min()

# COMMAND ----------

plt.figure(figsize=(20, 6))

sns.barplot(y= "price", x = "bedrooms", data = house, hue="waterfront")

# COMMAND ----------



# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20, 6))

sns.barplot(x="bedrooms", y="price", data=house, hue="waterfront", hue_order=[0, 1])

plt.show()


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns



plt.figure(figsize=(20, 6))

sns.barplot(x="bedrooms", y="price", data=house, hue="waterfront", hue_order=[0, 1], capsize = 0.25)


plt.show()


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns



plt.figure(figsize=(20, 6))

sns.barplot(x="bedrooms", y="price", data=house, hue="waterfront", hue_order=[0, 1], color = 'red')


plt.show()


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns



plt.figure(figsize=(20, 6))

sns.barplot(x="bedrooms", y="price", data=house, hue="waterfront", hue_order=[0, 1], color = 'red', palette='cividis', estimator=sum)


plt.show()


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns



plt.figure(figsize=(20, 6))

sns.barplot(x="bedrooms", y="price", data=house, hue="waterfront", hue_order=[0, 1], color = 'red', palette='cividis', estimator=np.median)


plt.show()


# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns
thing = house.head(1000)


plt.figure(figsize=(20, 6))

sns.boxplot(x="bedrooms", y="price", data=thing, hue="waterfront", hue_order=[0, 1])


plt.show()


# COMMAND ----------

sns.boxplot(x='price', data=house, width=0.5)

# COMMAND ----------

sns.boxplot(x='price', y='bedrooms', data=house)

# COMMAND ----------

sns.boxplot(x='price', y='bedrooms', data=thing, hue='waterfront')

# COMMAND ----------



# COMMAND ----------


