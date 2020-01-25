"""
Data import/export using the Eikon API. Requires a valid Eikon API key.
Source: https://github.com/yhilpisch/eikondataapi/blob/master/notebooks/
        by Dr. Yves Hilpisch
"""

import eikon as ek
import configparser as cp
import datetime as dt
import pandas as pd
import os
from pathlib import Path


# Set global variables.
cfg = cp.ConfigParser()
cfg.read('eikon_cfg.cfg')
ek.set_app_key(cfg['eikon']['app_id'])


def get_time_series(rics: list, fields: list, start_date: str, end_date: str) -> pd.DataFrame:
    """

    Retrieve time series data as Pandas DataFrame.
    Validate date input format as string.
    Not for stock data.
    :param rics: List of RIC:s to get.
    :param fields: List fields to get.
    :param start_date: Start date of time series.
    :param end_date: End date of time series.
    :return: Pandas DataFrame.
    """
    # Check date formats are YYYY-MM-DD.
    try:
        dt.datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('"start_date" has incorrect format.')
    try:
        dt.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('"end_date" has incorrect format.')

    data = ek.get_timeseries(rics, fields, start_date=start_date, end_date=end_date)
    return data


def get_data(rics: list, fields: list):
    """

    Eikon API call for data type file (not time series).
    Print any errors.
    :param rics: List of RIC:s to get.
    :param fields: List fields to get.
    :return: None.
    """
    data, err = ek.get_data(rics, fields)
    if err:
        print(err)
    return data


def make_data(rics: list, fields: list, name: str) -> None:
    """

    Get data from Eikon API and save to .csv (not time series data).
    :param rics: List of RIC:s to get.
    :param fields: List fields to get.
    :param name: File name to save (including ".csv" suffix).
    :return: None.
    """
    df = get_data(rics, fields)
    df.index.name = 'ID'
    to_csv(df, name)


def make_time_series(rics: list, fields: list, start_date: str, end_date: str, name: str) -> None:
    """

    Get time series data from Eikon API and save to .csv file.
    :param rics: List of RIC:s to get.
    :param fields: List fields to get (Eikon offers "CLOSE" as only option).
    :param start_date: Start date of time series (oldest date). Format "YYYY-MM-DD".
    :param end_date: End date of time series (newest date). Format "YYYY-MM-DD".
    :param name: New file name.
    :return: None.
    """
    df = get_time_series(rics, fields, start_date, end_date)
    df.dropna(inplace=True)
    to_csv(df, name, time_series=True)


def to_csv(df: pd.DataFrame, name: str, time_series=False) -> None:
    """

    Save a Pandas DataFrame as a .csv file in the "eikon_data_files" directory.
    :param df: Data to save as a .csv file.
    :param name: File name (no suffix).
    :param time_series: Is the file a time series type or not.
    :return: None.
    """
    abs_dir = os.path.dirname(__file__)
    if time_series:
        rel_dir = os.path.join(abs_dir, 'eikon_time_series_files')
    else:
        rel_dir = os.path.join(abs_dir, 'eikon_data_files')
    path = ''.join([rel_dir, '/' + name])

    df.to_csv(path, encoding='utf-8')
    print(' ')
    print('File "' + name + '" saved in directory "eikon_data_files".')


def read_data(name: str) -> pd.DataFrame:
    """

    Read .csv file by name from directory "eikon_data_files".
    :param name: File name (including suffix).
    :return: Pandas DataFrame.
    """
    import_dir = Path.cwd().joinpath('eikon_data_files')

    path = Path.joinpath(import_dir, Path(name))
    if path.exists():
        return pd.read_csv(path, sep=',')
    else:
        print('File type "' + name + '.csv' + ' does not exist. Aborted.')
        quit()


def read_time_series(name: str) -> pd.DataFrame:
    """

    Read .csv file by name from directory "eikon_time_series_files".
    :param name: File name (including suffix).
    :return: Pandas DataFrame.
    """
    import_dir = Path.cwd().joinpath('eikon_time_series_files')

    path = Path.joinpath(import_dir, Path(name))
    if path.exists():
        return pd.read_csv(path, sep=',', index_col=0, parse_dates=True)
    else:
        print('File type "' + name + '.csv' + ' does not exist. Aborted.')
        quit()


def read_config(rics: str, fields, time_series=False):
    """

    Read config files from directory "eikon_config_files".
    :param rics: Name of .csv file with RICS to get.
    :param fields: Name of .csv file with fields to get.
    :param time_series: Time series type file or not.
    :return: List(s).
    """
    import_dir = Path.cwd().joinpath('eikon_config_files')

    symb = []
    path = Path.joinpath(import_dir, Path(rics))
    if path.exists():
        s = pd.read_csv(path, sep=',')
        for column_name in s.columns:
            symb = s[column_name].tolist()
    else:
        print('File type "' + rics + '.csv' + ' does not exist. Aborted.')
        quit()

    if not time_series:
        flds = []
        path = Path.joinpath(import_dir, Path(fields))
        if path.exists():
            f = pd.read_csv(path, sep=',')
            for column_name in f.columns:
                flds = f[column_name].tolist()
        else:
            print('File type "' + fields + '.csv' + ' does not exist. Aborted.')
            quit()
        return symb, flds

    else:
        return symb
