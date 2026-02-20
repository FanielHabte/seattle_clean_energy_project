from .extract import run_extract   as extract
from .load import load_data        as load

pipeline_name = "energy_usage_db"

def run_ba_pipeline():
    extract()
    load(pipeline_name)

run_ba_pipeline()
