# Databricks notebook source
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

X = np.linspace(0,10,100)
Y= np.sin(X)

plt.plot(X,Y)
plt.xlabel("Points")
plt.ylabel("Sine  values")

# COMMAND ----------


