# Databricks notebook source
Iteration = 0
times = int(input("Enter how many times you want me to print hello: "))

while Iteration < times:
    print("#", Iteration, "Hello")
    Iteration = (Iteration + 1)

# COMMAND ----------

# MAGIC %md
# MAGIC **BIG DATA NOTES**

# COMMAND ----------

# 1st component of big data is velocity, where you sample very quickly. 
# 2nd component of big data is volume, where you have lots of data stored and ready to be used.
# 3rd component of big data is variety, where you have lots of different kinds of data.
# Basically, big data is about managing (like storing, getting, processing) of large amounts of different data very quickly.
# Big data uses CRUD operations (Create, Read, Update, Delete) which lets it quickly add new data, access it, update existing data, and delete unnessescary data.
# Big data lets you process lots of data, but it is up to you to plot and analyze the data correctly. Basically, what you do to the data makes it valuable
# Some examples of platforms that handle big data area: Spark, Hadoop, MongoDB, AWS, etc

# COMMAND ----------

# MAGIC %md
# MAGIC **PURPOSE OF AI NOTES**

# COMMAND ----------

# The ultimate goal of AI is to create an AI that can reason, think, plan, communicate, look at things, and be able to move things as well.
# The problem with getting AI to do this is the size of the search space. 
# The search space is all potential answers that an AI can give for a problem. The search space is basically all the answers for a problem, all of them that might work. For more complicated problems, there may be more and more solutions. Finding the most efficient and feasible solution is what the problem with the search space is.
# There are 2 main ways of navigating the search space, breadth first and depth first search

# COMMAND ----------

# MAGIC %md
# MAGIC **SPACE SEARCH NOTES**

# COMMAND ----------

# In breadth first navigation, the AI starts from 1 root node, then it tries its surrounding nodes, before moving on to the next level.
# BFN uses a queue to keep track of all the nodes it has looked at, and what nodes it hasn't examined yet. 
# Useful in finding the shortest path in something.
# Think of BFN as going door to door in a neighbourhood, trying to find one address by asking the people in the house.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In depth first navigation, the AI tries to explore as far as it can in one level, before moving to the next node.
# DFN uses a stack instead of a queue. Think of it as being lost in a maze, with a notebook. So whenever you go down one corridor, you mark each turn in your notebook. You follow the path all the way to its end, then you turn back. After you reach the start of that path, you mark it, so you don't end up going down it again. You repeat this process until you find the end. Except in DFN, the notebook is the stack

# COMMAND ----------

# MAGIC %md
# MAGIC **AI OVERVIEW**

# COMMAND ----------

# To start an AI model, you need to give it some data or inputs for it to be based on.
# Afer compiliing the data, you would apply a machine learning algorithim to it to to create an AI model
# You would then take new inputs and give them to the model, and get a prediction from the model. 
# Depending on how the model predicted, you may have to go back and tweak your algorithim, drop portions of data, etc.
# Machine learning depends on algorithims to analyze data
# Brief aside, what is the difference between Artificial Intelligence and Machine Learning?
# AI tries to do things humans can, with its ultimate goal of replicating human like behavior. Includes subfields like deep learning (more advanced predictions based on data), computer vision (computers being able to "see", like Tesla self driving cars), natural language processing (understanding and communicating with humans), etc
# ML is kind of basic. It makes predictions based on the information it gets, and becomes more accurate based on the quality of its information. ML is not explicity programmed to make its predictions, it just kinda learns on its own.


# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------



# COMMAND ----------



