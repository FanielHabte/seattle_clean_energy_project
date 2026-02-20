from .transform import cleaned_data
from ...sql.update_dw_table import create_replace_table
from ...sql.upload_file_to_volume import upload_to_volume
from ...helpers import get_config


def update_local_file(pipeline_name: str) -> None:
    pipeline_config = get_config(pipeline_name)
    local_file_path = pipeline_config["local_file_path"]
    df = cleaned_data()
    df.to_csv(local_file_path, index=False)


def load_data(pipeline_name: str) -> None:
    update_local_file(pipeline_name)
    upload_to_volume(pipeline_name)
    create_replace_table(pipeline_name)
