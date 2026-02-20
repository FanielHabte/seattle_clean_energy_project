from .extract import run_extract as extract
from .load import load_data as load

pipeline_name = "energy_usage_db"


def run_energy_pipeline():
    extract()
    load(pipeline_name)
    print("Energy usage pipeline run successfully!")
