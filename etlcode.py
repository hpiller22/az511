import pandas as pd
import requests
from datetime import datetime

az511_url = #redacted for privacy
#code get response redacted for privacy

if response.status_code == 200:
    print("Request was successful!")
else: 
    print(response.status_code + " Error")

data = response.json()
df = pd.DataFrame(data)

#unix time conversion
unix_time = df["Reported"].astype(int)
df["ReportTime"] = df["Reported"].astype(int).apply(datetime.fromtimestamp)
