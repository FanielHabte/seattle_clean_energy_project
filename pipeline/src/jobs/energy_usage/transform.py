import duckdb
import pandas as pd
from pathlib import Path


def consolidated_df():
    output_dir = Path("data/output")  # or anchor this to repo root (see below)
    files = list(output_dir.glob("*.csv"))

    df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
    return df


def transform_data(dataframe):
    query = """
        select distinct
            period::varchar(50)                as reporting_day
            , respondent::varchar(50)          as providers_alias
            , respondent_name::varchar(225)    as provider_name
            , timezone::varchar(50)            as provider_timezone
            , fueltype::varchar(50)            as fuel_type_alias
            , type_name::varchar(225)          as fuel_type_name
            , value::numeric(36,2)             as value
            , value_units::varchar(50)         as value_unit
            , snapshot_timestamp::varchar(50)  as snapshot_timestamp
            , dw_run_date::varchar(50)         as dw_run_date
        from data
        order by 1,2
    """
    transformed_df = duckdb.query_df(
        dataframe,
        "data",
        query,
    ).to_df()

    return transformed_df


def cleaned_data():
    df = consolidated_df()
    data = transform_data(df)

    print("Data transform completed successfully!")
    return data
