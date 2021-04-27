import pandas as pd
import geopandas as gpd
from shapely import wkt
from helpers import DataHelpers
import datetime


class Data:
    @classmethod
    def get_kansas(cls, df: pd.DataFrame) -> pd.DataFrame:
        return df[df['state'] == 'Kansas']

    @classmethod
    def read_covid_data(cls) -> pd.DataFrame:
        data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-recent.csv'
        df = pd.read_csv(data_url)
        kansas = cls.get_kansas(df)
        return kansas

    @classmethod
    def read_total_covid_data(cls) -> pd.DataFrame:
        data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
        df = pd.read_csv(data_url)
        kansas = cls.get_kansas(df)
        kansas.set_index('date', inplace=True)
        return kansas

    @classmethod
    def read_location_data(cls) -> pd.DataFrame:
        raw_counties = pd.read_csv('https://raw.githubusercontent.com/zumbaughca/Shapefiles/main/Counties.csv')
        raw_counties['geometry'] = raw_counties.geometry.apply(wkt.loads)
        ks = gpd.GeoDataFrame(raw_counties, geometry="geometry")
        return ks

    @classmethod
    def read_county_rolling(cls) -> pd.DataFrame:
        data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-counties-recent.csv'
        raw_data = pd.read_csv(data_url)
        kansas = cls.get_kansas(raw_data)
        return kansas

    @classmethod
    def read_state_rolling(cls) -> pd.DataFrame:
        data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-states.csv'
        raw_data = pd.read_csv(data_url)
        kansas = cls.get_kansas(raw_data)
        return kansas


class Dataset:
    covid_data = Data.read_covid_data()
    location_data = Data.read_location_data()
    county_rolling_avg = Data.read_county_rolling()

    @classmethod
    def get_last_day_data(cls, df: pd.DataFrame) -> pd.DataFrame:
        latest_data = DataHelpers.get_latest(df)
        return DataHelpers.create_plot_data(loc=cls.location_data, loc_index='NAME',
                                            data=latest_data, data_index='county')

    @classmethod
    def get_aggregate_sum(cls) -> pd.DataFrame:
        aggregate = DataHelpers.sum_by_day(cls.covid_data)
        aggregate['new_monthly_cases'] = aggregate['cases'] - aggregate.iloc[0]['cases']
        aggregate['new_monthly_deaths'] = aggregate['deaths'] - aggregate.iloc[0]['deaths']
        return aggregate

    @classmethod
    def get_sum_by_county(cls) -> pd.DataFrame:
        df = cls.covid_data[['county', 'cases', 'deaths']]
        df['new_cases'] = df.groupby('county')['cases'].diff().fillna(0)
        df['new_deaths'] = df.groupby('county')['deaths'].diff().fillna(0)
        df = df.groupby('county').mean()
        df['county'] = df.index
        return DataHelpers.create_plot_data(loc=cls.location_data, loc_index='NAME',
                                            data=df, data_index='county')


    @classmethod
    def get_total_sum_data(cls) -> pd.DataFrame:
        return Data.read_total_covid_data()
