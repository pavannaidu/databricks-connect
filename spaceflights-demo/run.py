# Databricks notebook source
%pip install -r "requirements.txt"

# COMMAND ----------
dbutils.library.restartPython()

# COMMAND ----------
import sys
print(sys.version)

# COMMAND ----------
%load_ext kedro.ipython

# COMMAND ----------
%reload_kedro --env=databricks

# COMMAND ----------
session.run()