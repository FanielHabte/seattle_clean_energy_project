from databricks.sdk import WorkspaceClient
from ..helpers import get_config


def upload_to_volume(pipeline_type: str) -> None:

    pipeline_config = get_config(pipeline_type)
    local_file_path = pipeline_config["local_file_path"]
    path_volume = pipeline_config["volume_path"]

    databricks_config = get_config("databricks")
    host_name = databricks_config["hostname"]
    api_token = databricks_config["token"]

    w = WorkspaceClient(host=host_name, token=api_token)
    with open(local_file_path, "rb") as f:
        w.files.upload(path_volume, f)
