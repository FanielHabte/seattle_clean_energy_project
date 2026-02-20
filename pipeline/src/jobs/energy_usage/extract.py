import pandas as pd
import requests as rq
from ...helpers import (
    get_config,
    generate_time_period,
    generate_run_report,
    get_start_date,
)

pipeline_config = get_config("energy_usage_db")
api_key = pipeline_config["api_key"]
url = pipeline_config["api_url"]
data_start_date = get_start_date()  # Format -> YYYY-MM-DD E.g "2026-02-01"


def pull_daily_data():
    iteration = 1
    offset = 0
    length = 5000
    data = []
    flag = True

    while flag:
        response = rq.get(
            f"{url}&start={data_start_date}&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset={offset}&length={length}&api_key={api_key}"
        )
        status = response.status_code
        if status == 200:
            json_response = response.json()["response"]["data"]
            for records in json_response:
                data.append(records)

            iteration += 1
            offset += length

        if len(json_response) == 0 or json_response is None:
            flag = False
            raise RuntimeError("No new records found.")

    df = pd.DataFrame(data)
    df["snapshot_timestamp"] = generate_time_period("timestamp")
    df["dw_run_date"] = generate_time_period("date")

    return df


def run_extract() -> None:
    # Start time
    start_time = generate_time_period(period_type="timestamp")
    df = pull_daily_data()
    data_end_date = max(df["period"])
    df.to_csv(f"data/output/{data_end_date}.csv", index=False)
    end_time = generate_time_period(period_type="timestamp")
    row_count = len(df)

    generate_run_report(
        run_start_time=start_time,
        run_end_time=end_time,
        from_date=data_start_date,
        to_date=data_end_date,
        row_count=row_count,
    )
    print("Data extract completed successfully!")


if __name__ == "__main__":
    run_extract()
    print("Data extract completed successfully!")
