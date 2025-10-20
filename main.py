import requests
import os 

start_date = "2025-10-17T00"
end_date = "2025-10-18T00"
api_key = "7glYQjzdiuWWQ8pCgbyWRzg8iMPtgDJyZgfcJXg4"
url = f"https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/?frequency=hourly&data[0]=value&facets[respondent][]=SCL&start={start_date}&end={end_date}&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=10&api_key={api_key}"

response = requests.get(url)
json_response = response.json()

list_data = []
for record in json_response["response"]["data"]:
    list_data.append(record)
    

# [
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AECI",
#         "respondent-name": "Associated Electric Cooperative, Inc.",
#         "fueltype": "COL",
#         "type-name": "Coal",
#         "value": "1614",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AECI",
#         "respondent-name": "Associated Electric Cooperative, Inc.",
#         "fueltype": "NG",
#         "type-name": "Natural Gas",
#         "value": "841",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AECI",
#         "respondent-name": "Associated Electric Cooperative, Inc.",
#         "fueltype": "WND",
#         "type-name": "Wind",
#         "value": "65",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVA",
#         "respondent-name": "Avista Corporation",
#         "fueltype": "NG",
#         "type-name": "Natural Gas",
#         "value": "341",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVA",
#         "respondent-name": "Avista Corporation",
#         "fueltype": "OTH",
#         "type-name": "Other",
#         "value": "118",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVA",
#         "respondent-name": "Avista Corporation",
#         "fueltype": "SUN",
#         "type-name": "Solar",
#         "value": "2",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVA",
#         "respondent-name": "Avista Corporation",
#         "fueltype": "WAT",
#         "type-name": "Hydro",
#         "value": "389",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVA",
#         "respondent-name": "Avista Corporation",
#         "fueltype": "WND",
#         "type-name": "Wind",
#         "value": "171",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVRN",
#         "respondent-name": "Avangrid Renewables, LLC",
#         "fueltype": "NG",
#         "type-name": "Natural Gas",
#         "value": "425",
#         "value-units": "megawatthours",
#     },
#     {
#         "period": "2025-09-07T00",
#         "respondent": "AVRN",
#         "respondent-name": "Avangrid Renewables, LLC",
#         "fueltype": "SUN",
#         "type-name": "Solar",
#         "value": "0",
#         "value-units": "megawatthours",
#     },
# ]

    
print(list_data)