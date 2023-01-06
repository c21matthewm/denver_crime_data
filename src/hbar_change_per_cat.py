import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium import plugins
from scipy import stats



def hbar_crime_increase_by_category(df):

    offense_cat_list = list(df['OFFENSE_CATEGORY_ID'].unique())
    # offense_cat_list
    year_list = list(df['OCCURRENCE YEAR'].unique())
    # year_list

    crime_by_cat_year = []
    crime_by_cat_df = pd.DataFrame(index=offense_cat_list, columns=year_list)
    # crime_by_cat_df

    for i in year_list:
        for j in offense_cat_list:
            x = df[(df['OFFENSE_CATEGORY_ID'] == j) & (df['OCCURRENCE YEAR'] == i)].count()['incident_id']
            crime_by_cat_year.append(x)
        crime_by_cat_df[i] = crime_by_cat_year
        crime_by_cat_year = []
    crime_by_cat_df.sort_index(axis=1, ascending=True, inplace=True)
    crime_by_cat_df.sort_values(by=[2017], ascending=False, inplace=True)
    
    
    slope_list = []

    for i in range(len(offense_cat_list)):
        slope, intercept, r, p, se = stats.linregress(crime_by_cat_df.transpose().index, crime_by_cat_df.iloc[i])
        slope_list.append(slope)
    # slope_list


    fig, ax = plt.subplots()

    ax.barh(offense_cat_list, slope_list)
    ax.set_title('Average Increase per Year in Each Crime Category')
    ax.set_xlabel('Average Increase in Number of Crimes per Year')
    ax.set_ylabel('Crime Category')
    ax.tick_params(axis='x', direction='in', length=266, width=0.25)

    return ax