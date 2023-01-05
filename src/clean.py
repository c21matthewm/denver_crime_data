import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium import plugins
from scipy import stats



# Read file from .csv and create dataframe with given sample size

def create_dataframe_and_sample_from_csv(filepath, samplesize=None):
    if samplesize == None:
        crime_data_df = pd.read_csv(filepath)
    elif samplesize > 100000:
        crime_data_df = pd.read_csv(filepath)
    else:
        crime_data_df = pd.read_csv(filepath).sample(samplesize)
    return crime_data_df



# Clean dataset: removing uneeded columns, adding 'Year' and 'Month' columns to df, removing years with incomplete data ##

def clean_dataset(df):
    df.drop(["LAST_OCCURRENCE_DATE", 'OFFENSE_CODE_EXTENSION', 'IS_CRIME', 'IS_TRAFFIC', 'GEO_X', 'GEO_Y', 'PRECINCT_ID'], axis=1, inplace=True)
    df['FIRST_OCCURRENCE_DATE'] = pd.to_datetime(df['FIRST_OCCURRENCE_DATE'])
    df['OCCURRENCE YEAR'] = df['FIRST_OCCURRENCE_DATE'].dt.year
    df['OCCURRENCE MONTH'] = df['FIRST_OCCURRENCE_DATE'].dt.month
    df = df[df['OCCURRENCE YEAR'] < 2022]
    return df



if __name__ == "__main__":
    crime_data = create_dataframe_and_sample_from_csv('data/crime.csv')
    crime_df_cleaned = clean_dataset(crime_data)