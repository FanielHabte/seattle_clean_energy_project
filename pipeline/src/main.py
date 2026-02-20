from scripts.extract import run_extract
from scripts.load import load_data
from .helpers import (
    get_config,
)

### SQL Engine Confi Details ###
databricks_config = get_config()["databricks"]
hostname = databricks_config["hostname"]
token = databricks_config["token"]
path = databricks_config["path"]

### Energy Usage Table Details ###
local_path = databricks_config["local_file_path"]
volume_path = databricks_config["volume_path"]
table_name = databricks_config["table_name"]
columns = "reporting_day STRING, providers_alias STRING, provider_name STRING, provider_timezone STRING, fuel_type_alias STRING, fuel_type_name STRING, value DOUBLE, value_unit STRING, snapshot_timestamp STRING, dw_run_date STRING"

### BA Details ###

def main():
    # run_extract()
    load_data()
    

if __name__ == "__main__":
    main()
    print("Pipeline run end to end")