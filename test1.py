import pandas as pd

# Example 1: Convert string to datetime
date_str = '2022-01-01'
date_dt = pd.to_datetime(date_str)
print(date_dt)  # Output: 2022-01-01 00:00:00

# Example 2: Convert list of strings to datetime
date_list = ['2022-01-01', '2022-01-02', '2022-01-03']
date_dt_list = pd.to_datetime(date_list)
print(date_dt_list)

# Example 3: Convert with errors='coerce'
date_str_with_error = ['2022-01-01', 'invalid_date', '2022-01-03']
date_dt_with_error = pd.to_datetime(date_str_with_error, errors='coerce')
print(date_dt_with_error)

# Example 4: Specify format
date_str_custom_format = '01-01-2022'
date_dt_custom_format = pd.to_datetime(date_str_custom_format, format='%d-%m-%Y')
print(date_dt_custom_format)

# Example 5: Specify unit
timestamp = 1640995200  # Unix timestamp for '2022-01-01 00:00:00'
date_dt_from_timestamp = pd.to_datetime(timestamp, unit='s')
print(date_dt_from_timestamp)
test2.py
