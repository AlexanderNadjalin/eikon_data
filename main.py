"""

Create data files or time series files from Eikon's Python API.

"Data files" are files with a snapshot of data such as current price, company sector, instrument maturity etc.
"Time series files" are historical prices for given instruments. Eikon has a limited number of fields via the API.

Pre-requisites:
    * A running Eikon desktop application.
    * A valid Eikon API key in the "eikon_cfg.cfg" file.
"""

import eikon_data_import as edi


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
    start_date = '2019-01-02'
    # Latest date
    end_date = '2020-01-24'
    # Field to get
    field = ['CLOSE']
    # File name to save time series as (including ".csv" ending)
    name_time_series = 'Swaps_time_series.csv'

    # Create new data file or new time series file:
    edi.create_data_file(rics_cfg, fields_cfg, name_data)
    edi.create_time_series_file(rics_cfg, field, start_date, end_date, name_time_series)

    # Read data:
    df_dt = edi.read_data(name_data)
    # Read time series:
    df_ts = edi.read_time_series(name_time_series)
