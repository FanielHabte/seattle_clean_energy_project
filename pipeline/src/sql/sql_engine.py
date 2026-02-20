from databricks import sql
from ..helpers import get_config

databricks_config = get_config("databricks")
host_name = databricks_config["hostname"]
http_path = databricks_config["path"]
api_token = databricks_config["token"]

def db_sql_engine():
    connection = sql.connect(
        server_hostname=host_name, http_path=http_path, access_token=api_token
    )
    cursor = connection.cursor()

    return cursor