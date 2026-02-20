import yaml
import time
import json
from datetime import datetime, timedelta


def get_config(pipeline_type):
    config_path = "pipeline/src/config/config.yaml"
    with open(config_path, "r") as config_file:
        data = yaml.safe_load(config_file)

        if pipeline_type in data.keys():
            return data[pipeline_type]
        else:
            raise RuntimeError(
                f"Please input a valid config key. Here are the expected keys {data.keys()}"
            )


def generate_time_period(period_type: str) -> str:
    if period_type == "date":
        period = time.strftime("%Y-%m-%d", time.localtime())
    elif period_type == "timestamp":
        period = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    else:
        raise RuntimeError("Please choose a valid input [date or timestamp]")

    return period


def generate_run_report(
    run_start_time: str,
    run_end_time: str,
    from_date: str,
    to_date: str,
    row_count: int,
):

    json_path = get_config("file_path")["json_logs"]

    report = {
        "run_id": f"{run_end_time}_usa_daily_energy_usage",
        "pipeline": "USA Energy Daily Usage",
        "status": "success",
        "rows_count": row_count,
        "events": [
            {
                "type": "job_run",
                "start": run_start_time,
                "end": run_end_time,
            },
            {
                "type": "data_refreshed",
                "from": from_date,
                "to": to_date,
            },
        ],
    }

    with open(json_path, "r") as j_file:
        run_log_list = json.load(j_file)
        run_log_list.append(report)

    with open(json_path, "w") as j_file:
        json.dump(run_log_list, j_file, indent=4)


def get_start_date():

    json_path = get_config("file_path")["json_logs"]

    with open(json_path, "r") as j_file:
        run_log_list = json.load(j_file)
        to_date_list = [log["events"][1]["to"] for log in run_log_list]
        most_recent_date = (
            datetime.strptime(max(to_date_list), "%Y-%m-%d").date() + timedelta(days=1)
        ).isoformat()

    return most_recent_date


if __name__ == "__main__":
    print(get_config("energy_usage_db")["api_key"])
