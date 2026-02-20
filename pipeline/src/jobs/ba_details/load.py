from ...sql.upload_file_to_volume import upload_to_volume
from ...sql.update_dw_table import create_replace_table


def load_file_update_dw_table(pipeline_type):
    upload_to_volume(pipeline_type)
    create_replace_table(pipeline_type)

    print("DW table has been updated.")
