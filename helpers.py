from datetime import date
from datetime import timedelta
import pandas as pd


class DataHelpers:
    @classmethod
    def select_date(cls, date, df) -> pd.DataFrame:
        return df[df['date'] == date]

    @classmethod
    def get_latest(cls, df: pd.DataFrame) -> pd.DataFrame:
        previous = date.today() - timedelta(days=2)
        current = date.today() - timedelta(days=1)
        previous_df = df[df['date'] == previous.__str__()]
        current_df = df[df['date'] == current.__str__()]
        current_df.set_index('county', inplace=True, drop=False)
        previous_df.set_index('county', inplace=True, drop=False)
        current_df['new_cases'] = current_df['cases'] - previous_df['cases']
        current_df['new_deaths'] = current_df['deaths'] - previous_df['deaths']
        return current_df

    @classmethod
    def create_plot_data(cls, loc: pd.DataFrame, loc_index: str, data: pd.DataFrame, data_index: str) -> pd.DataFrame:
        loc[loc_index] = loc[loc_index].str.lower()
        data[data_index] = data[data_index].str.lower()
        merged = loc.set_index(loc_index).join(data.set_index(data_index))
        return merged

    @classmethod
    def sum_by_day(cls, df: pd.DataFrame):
        return df.groupby('date').sum()

    @classmethod
    def sum_by_county(cls, df: pd.DataFrame) -> pd.DataFrame:
        return df.groupby('county').sum()