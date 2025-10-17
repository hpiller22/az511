import pandas as pd
import requests
from datetime import datetime

az511_url = [api url]

params = {"key": [api key] }
response = requests.get([api_url]", params=params)

if response.status_code == 200:
    print("Request was successful!")
else: 
    print(response.status_code + " Error")

data = response.json()
df = pd.DataFrame(data)
df["Reported"] = pd.to_numeric(df["Reported"], errors="coerce")
df = df[df["Reported"].notna() & (df["Reported"] > 0)]

unix_time = df["Reported"].astype(int)
df["ReportTime"] = df["Reported"].astype(int).apply(datetime.fromtimestamp)
