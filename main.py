import requests
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime as dt

def get_max_date(csv_file):
    df = pd.read_csv(csv_file)
    time_format = "%Y-%m-%dT%H"
    max_date = pd.to_datetime(df.period, format=time_format).max()
    max_date_str = dt.strftime(max_date, time_format)
    return max_date_str

load_dotenv()

file_path = "data/EIA_Data.csv"
time_format = "%Y-%m-%dT%H"
start_date = get_max_date(file_path)
end_date = dt.strftime(dt.now(), format=time_format)
api_key = os.getenv("EIA_APP_TOKEN")
offset_value = 0
limit = 5000

url = f"https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/?frequency=hourly&data[0]=value&facets[respondent][]=SCL&start={start_date}&end={end_date}&sort[0][column]=period&sort[0][direction]=asc&offset={offset_value}&length={limit}&api_key={api_key}"
flag = True
    
try:
    response = requests.get(url)
    json_response = response.json()["response"]["data"]
except requests.exceptions.HTTPError as errh:
    print("Error: HTTP Error")
    print(errh.args[0])
except requests.exceptions.ReadTimeout as errrt:
    print("Error: Time out")
except requests.exceptions.ConnectionError as conerr:
    print("Error: Connection")
except requests.exceptions.RequestException as errex:
    print("Error: Exception request")
else:
    df = pd.DataFrame(json_response)
    df.period = pd.to_datetime(df.period, format=time_format)
    max_date = pd.to_datetime(start_date, format=time_format)
    df_to_append = df.loc[df["period"] > max_date].copy().dropna(how="all")
    df_to_append.period = df.period.dt.strftime(time_format)
    
if df_to_append.empty:
    print("No new rows to append.")
else:
    df_to_append.to_csv(
        file_path,
        mode="a",
        index=False,
        header=False, 
        lineterminator="\n",
    )
