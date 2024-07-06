# Databricks notebook source
import pandas as pd
titanic = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/titanic.csv")
titanic

# COMMAND ----------

titanic.head()

#.head()
# displays the rows specified in the brackets. defaults to first 5

# COMMAND ----------

titanic.tail()

#.tail()
# displays the rows specified in the brackets. defaults to last 5

# COMMAND ----------

titanic.shape

#.shape
# show you the amount of rows and columns in the dataframe. ie, 1309, 14

# COMMAND ----------

type(titanic)

# type()
# show you the type of whatever you put in the brackets

# COMMAND ----------

type(titanic.shape)

# type()
# as you can see, there is a tuple

# COMMAND ----------

type(titanic.head())

# type()
# as you can see, the .head() method is still a dataframe

# COMMAND ----------

titanic.info()

#.info()
# gives you the number of rows, columns, datatypes, column names etc.

# COMMAND ----------

import pandas as pd
netflix = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/netflix_titles.csv", sep="|")
netflix

#"/dbfs/FileStore/datavisualization-in-databricks/data/dataframename.csv", sep "enter seperator"
# used when you CSV file is not seperated by commas

# COMMAND ----------

titanic["name"]

# loading columns
# there are 2 ways to load a specific column, this is the official way. in both ways, the specific column you have selected will be opened.

# COMMAND ----------

titanic.name

# loading columns
# there are 2 ways to load a specific column, this is the second, easier way. in both ways, the specific column you have selected will be opened.

# COMMAND ----------

titanic.describe()

#.describe()
# gives you a breakdown of numeric columns, such as their total count, mean, etc
# so far, describe only includes columns that have numeric values in them

# COMMAND ----------

titanic.describe(include=["object"])

#.describe()
# putting include in the brackets lets you include the specified datatype. 
# in this case it is objects (letters and numbers both)

# COMMAND ----------

titanic.mean()


#.mean()
# finds the mean of the selected dataframe. includes objects as well, so you may get some weird results

# COMMAND ----------

titanic.mean(numeric_only=True)


#.mean()
# using this, we calculate the mean of only numbers

# COMMAND ----------

titanic.median()

#.median()
# finds the median of the selected dataframe. includes objects as well, so you may get some weird results

# COMMAND ----------

titanic.median(numeric_only=True)

#.median()
# using this, we calculate the median of only numbers

# COMMAND ----------

titanic.mode()

#.median()
# finds the median of the selected dataframe. includes objects as well, so you may get some weird results

# COMMAND ----------

titanic.mode(numeric_only=True)

#.median()
# using this, we calculate the mode of only numbers

# COMMAND ----------

titanic.unique()

#.unique
# this should display all the values in a dataframe, but it is meant to be called on 1 specific column, not the whole frame.

# COMMAND ----------

titanic["boat"].unique()

#.unique
# this should display all the values in a dataframe, but it is meant to be called on 1 specific column, not the whole frame.

# COMMAND ----------

import pandas as pd
houses = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/kc_house_data.csv")
houses

# COMMAND ----------

houses.grade.unique()

#.unique()
# shows all the unique values for the grade column

# COMMAND ----------

houses.price.nlargest()

#.nlargest()
# similar to .head(), nlargest will show you the 5 largest values in the specified column, in descending order. this means that the highest value will be shown first, then the second highest, then third, etc. you can specify how many values are shown by entering a number in the brackets

# COMMAND ----------

houses.price.nlargest(ascending=False)

#.nlargest()
# now it will print fifth highest, then fourth highest, then third highest etc. can also be done to .nsmallest()

# COMMAND ----------


houses.price.nlargest(12, keep="all")

#.nlargest()
# this code will find the 12 highest values in the dataset, and print all of them in the event of a tie. can also be done to .nsmallest()

# COMMAND ----------

houses.price.nsmallest()

#.nsmallest()
# does the same thing as nlargest, except it shows the smallest values in the specified column

# COMMAND ----------

houses.max()

#.max()
# shows the highest value in each column for the entire houses dataframe

# COMMAND ----------

houses.min()

#.min()
# shows the lowest value in each column for the entire houses dataframe

# COMMAND ----------

titanic["pclass"].value_counts()

#.value_counts()
# shows how many types each price appears in the column pclass. can be used in any combination, ie:

# COMMAND ----------

titanic["pclass"].head().value_counts()

#.value_counts
#shows that in the firt 5 row of the titanic dataframe, pclass 1 comes up 5 times.

# COMMAND ----------

titanic["pclass"].plot()

#.plot
# plots a graph of the data. you can change the type of graph, ie bar, pie, line, etc

# COMMAND ----------

titanic["pclass"].value_counts().plot()

#.plot()
#example of plot being used on something

# COMMAND ----------

import pandas as pd
btc = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/coin_Bitcoin.csv")
btc

# COMMAND ----------

edit = btc.set_index("Date")
edit
# .set_index
# in this we have set the index as date, so now the dataframe is organized by date 

# COMMAND ----------

import pandas as pd
df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv", index_col = 0)
df

# index_col = "number"
# this is similar to the sep="" from earlier. what this does is that it sets the first column as the index. so now the frame is ordered by country name, instead of just 0, 1, 2, 3, etc

# COMMAND ----------

import pandas as pd
df = pd.read_csv("/dbfs/FileStore/datavisualization-in-databricks/data/world_happiness_report_2021.csv")
df


# index_col = "number"
# this is wha the world_happiness_report_csv looks like before we set the index to 0. titanic. 

# COMMAND ----------

titanic["name"].sort_values()

#.sort_values()
# this sorts selected column in ascending order


# COMMAND ----------

titanic.age.sort_index()

#.sort_index()
# sorts selected column in index by ascending order. 

# COMMAND ----------

titanic.sort_values("name", key=lambda col: col.str.lower())
# .sort_values
# this code is another way to sort values with strings in them. it converts them all to lowercase. normally databrickspython sorts capital letters alphabteically, then moves on to small letters. by converting them all to lowercase, there are no errors in the sorting.

# COMMAND ----------

titanic.iloc[144:145]

#.iloc
# finds the row between rows 144 & 145 and prints it. 

# COMMAND ----------

titanic.sex
titanic.sex == 'female'
titanic[titanic.sex == 'female']

#using boolean indexing
#this only displays the female titanic passengers. we can see 466 rows out of the 1309 total
# this will work on any column of the dataframe, you just have to set the == to something valid for the column

# COMMAND ----------

titanic[titanic.age == "18"]

#using boolean indexing
# numbers in the column are considered strings, so you have to wrap them in quotes
# so this prints all passengers of the titanic who are exactly 18 years old.

# COMMAND ----------

titanic[titanic.pclass != 1]
titanic

# using boolean indexing
# this will print all people whos pclass isn't 1. so all pclass 2 and pclass 3 people

# COMMAND ----------

houses["bedrooms"].between(5, 7)

# .between()
# checks that the values in the "bedrooms" column are between 5 and 7. 5 and 7 are also included


# COMMAND ----------

# MAGIC %md
# MAGIC
