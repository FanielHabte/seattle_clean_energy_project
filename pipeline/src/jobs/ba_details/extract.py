import requests
from ...helpers import get_config

def pull_ba_details(pipeline_type):

    pipeline_config = get_config(pipeline_type)
    api_url = pipeline_config["api_url"]
    
    response = requests.get(api_url)
    status = response.status_code
    if status == 200:
        ba_data = response.json()["results"]
        print("All data has been pulled.")
        return ba_data
    else:
        raise RuntimeError("BA data pull status returned 200, please check the reason")


if __name__ == "__main__":
    ...
