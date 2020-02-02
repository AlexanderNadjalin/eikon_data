# eikon_data
This simple module allows us to create .csv files with financial data from Eikon's [Python API](https://developers.refinitiv.com/eikon-apis/eikon-data-api "Eikon's Python API").

The files are of two types - data files and time series files. Data files are a snapshot of a single RIC and the data it contains right now. There are many fields and data types available. The time series files can contain historical price data for a large number of RICs.

The files can be used for data import and analysis. Time series files can be imported andvisualized with another module [swap_curves_with_bqplot](https://github.com/AlexanderNadjalin/swap_curves_with_bqplot).

## Prerequisites
To use this module we need to have a few things in place:

* A running Eikon desktop application.
* A valid Eikon API key in the "eikon_cfg.cfg" file.

## Usage
For both types of files there are a few common parameters that we need.

* A .csv file with the RICs in a column.
* A .csv file with the fields in a column.

### Create data file
We use the function 

```create_data_file(rics_cfg, fields_cfg, name_data)```

where:

```rics_cfg``` is the name of .csv file with RICs. Located in directory "eikon_data/eikon_config_files/".

```fields_cfg``` is the name of the .csv file with fields. Located in directory "eikon_data/eikon_config_files/". 

```name_data``` is the name of the output file containing the Eikon data. Located in directory "eikon_data/eikon_data_files/".

### Create time series file
We use the function

```create_time_series_file(rics_cfg, field, start_date, end_date, name_time_series)```

where:
```rics_cfg``` is the name of .csv file with RICs. Located in directory "eikon_data/eikon_config_files/".

```field``` is the name of the .csv file with fields. Located in directory "eikon_data/eikon_config_files/". 

```start_date```is the earliest date. Format "YYYY-MM-DD".

```ènd_date```is the latest date. Format "YYYY-MM-DD".

```name_time_series``` is the name of the output file containing the Eikon data. Located in directory "eikon_data/eikon_data_files/".

### Example of results
Data file:

<img width="700" src="/images/Data_example.png" />

Time series file:

<img width="700" src="/images/Time_series_example.png" />
