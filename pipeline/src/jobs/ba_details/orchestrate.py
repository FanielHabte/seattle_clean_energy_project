from .extract import pull_ba_details as extract
from .transform import transform_data as transform
from .load import load_file_update_dw_table as load

pipeline_name = "ba_metadata_db"
structure_df = {
    "id": [],
    "name": [],
    "country": [],
    "state": [],
    "city": [],
    "address": [],
    "telephone": [],
    "source": [],
    "website": [],
}


def run_ba_pipeline():
    api_json_response = extract(pipeline_name)
    transform(api_json_response, structure_df)
    load(pipeline_name)
    print("BA data pipeline run successfully!")


if __name__ == "__main__":
    run_ba_pipeline()
