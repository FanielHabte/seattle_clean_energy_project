import pandas as pd
from ...helpers import generate_time_period

def transform_data(ba_api_response, structure_df):
    for details in ba_api_response:
        for df_key in structure_df.keys():
            detail = details[df_key]
            structure_df[df_key].append(detail)

    df = pd.DataFrame(structure_df)
    df["refresh_date"] = generate_time_period("timestamp")
    df.to_csv("data/meta/ba_details_table.csv", index=False)
    
    print("Data has been transformed and local CSV file has been updated.")

if __name__ == "__main__":
    ...