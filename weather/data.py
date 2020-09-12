from pathlib import Path
from pandas import DataFrame, read_csv


def floatify(s: str) -> float:
    return float(s.split()[0])


wx_map = {
    'Temperature': floatify,
    'Dew Point':   floatify,
    'Humidity':    floatify,
    'Wind Speed':  floatify,
    'Wind Gust':   floatify,
    'Pressure':    floatify,
    'Precip.':     floatify,
} 


def get_dataframe(path: Path) -> DataFrame:
    return read_csv(path, 
                    converters = wx_map,
                    parse_dates={'datetime': ['Date', 'Time']})