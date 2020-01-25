import eikon_data_import as edi


def create_data_file(rics_conf: str, fields_conf: str, file_name: str) -> None:
    rics, fields = edi.read_config(rics_conf, fields_conf, time_series=False)
    edi.make_data(rics, fields, file_name)


def create_time_series_file(rics_conf: str, fields_conf: list, start_dt: str, end_dt: str, file_name: str) -> None:
    rics = edi.read_config(rics=rics_conf, fields=None, time_series=True)
    edi.make_time_series(rics, fields_conf, start_dt, end_dt, file_name)


if __name__ == '__main__':
    # Common parameters
    # RICs to get
    rics_cfg = 'swap_rics.csv'

    # Data file specific:
    # Fields to get.
    fields_cfg = 'swap_fields.csv'
    # File name to save data as (including ".csv" ending)
    name_data = 'Swaps.csv'

    # Time series specific:
    # Earliest date
    start_date = '2020-01-22'
    # Newest date
    end_date = '2020-01-24'
    # Field to get
    field = ['CLOSE']
    # File name to save time series as (including ".csv" ending)
    name_time_series = 'Swaps_time_series.csv'

    # Create new data file or new time series file:
    # create_data_file(rics_cfg, fields_cfg, name_data)
    # create_time_series_file(rics_cfg, field, start_date, end_date, name_time_series)

    # Read data:
    df_dt = edi.read_data(name_data)
    # Read time series:
    # df_ts = edi.read_time_series(name_time_series)
