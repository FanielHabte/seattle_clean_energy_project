from .jobs.ba_details.orchestrate import run_ba_pipeline as ba_pipeline
from .jobs.energy_usage.orchestrate import run_energy_pipeline as energy_pipeline


def run_all_pipeline():
    ba_pipeline()
    energy_pipeline()

run_all_pipeline()