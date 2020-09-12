from pathlib import Path
from pandas import DataFrame, read_csv


def retrieve_data(path: Path) -> DataFrame:
    not_needed = ['Days ago', 
                  'Last error',
                  '2nd last error',
                  '3rd last error',
                  '4th last error',]
    return read_csv(path, parse_dates=['Date']).drop(not_needed, axis=1)