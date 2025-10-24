import psycopg as py
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USERNAME")
dbname = os.getenv("DBNAME")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
csv_file_path = "data/EIA_Data.csv"

conn = py.connect(
    f"dbname={dbname} user={user} host={host} password={password} port={port}"
)
cur = conn.cursor()

csv_data = pd.read_csv(csv_file_path)
df = csv_data[
    [
        "period",
        "respondent",
        "respondent-name",
        "fueltype",
        "type-name",
        "value",
        "value-units",
    ]
]
df = df.where(df.notna(), None)

with cur.copy(
    "COPY public.eia_raw_data (period, respondent, respondent_name, fueltype, type_name, value, value_units) FROM STDIN"
) as copy:
    for record in df.itertuples(index=False, name=None):
        copy.write_row(record)

conn.commit()
conn.close()

