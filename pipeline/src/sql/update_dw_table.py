from .sql_engine import db_sql_engine
from ..helpers import get_config


def create_replace_table(pipeline_type: str) -> None:
    cursor = db_sql_engine()

    pipeline_config = get_config(pipeline_type)
    table_name = pipeline_config["table_name"]
    path_volume = pipeline_config["volume_path"]
    column_details = pipeline_config["column_details"]

    cursor.execute(
        f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM read_files(
            "{path_volume}",
            format => "csv",
            header => "true",
            schema => "{column_details}"
        );
        """,
    )
    cursor.close()
