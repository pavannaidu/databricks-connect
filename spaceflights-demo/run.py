# Databricks notebook source
%pip install -r "requirements.txt"


# COMMAND ----------
%load_ext kedro.ipython

# COMMAND ----------
%reload_kedro --env=databricks

# COMMAND ----------
session.run()