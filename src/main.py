from fastapi import FastAPI
import redis
import pandas as pd
import numpy as np
import sys
import plotly.express as px


# app = FastAPI()

# r = redis.Redis(host="redis", port=6379)

# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# # debugpy.wait_for_client()

# @app.get("/")
# def read_root():
#     r.incr("hits")    
#     return {"hello": "world!"}


# @app.get("/hits")
# def read_root():
#     return {"number of hits": r.get("hits")}

# @app.get("/cc")
# def read_root():
#     data = pd.read_csv("credit_card.csv")
#     print(data.head())
#     print(data.isnull().sum())
#     print(data.type.value_counts())
#     type = data["type"].value_counts()
#     transactions = type.index
#     quantity = type.values
    
#     figure = px.pie(data, 
#              values=quantity, 
#              names=transactions,hole = 0.5, 
#              title="Distribution of Transaction Type")
#     figure.show()