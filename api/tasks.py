import csv
from celery import Celery
import pandas as pd
import requests

app = Celery('tasks', broker='redis://localhost//')

@app.task
def process_csv_task(path):
    for chunk in pd.read_csv(path, header=0, chunksize=100):
        for row in chunk.iterrows():

            row = dict(row[1])
            print("processing: ", row)
            payload = {"name": row["from"],
                       "referer": row["to"],
                       "amount": row["amount"],
                       "date": row["date"] + "T00:00"}
            r = requests.post("http://127.0.0.1:8000/transactions/", data=payload)
            print(r)
            print(r.text)
