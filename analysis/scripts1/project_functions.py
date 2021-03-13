import pandas as pd 
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file, delimiter=";")
          .rename(
              columns={"PT08.S4(NO2)":"Tungsten Oxide", "PT08.S1(CO)":"Tin Oxide", "C6H6(GT)":"Benzene(GT)", "NO2(GT)":"Tungsten Oxide(GT)", "T": "Temperature", "RH":"Relative Humidity", "AH":"Absolute Humidity", "Time":"Hour of Day"}
              )
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .drop(columns=["NMHC(GT)", "PT08.S2(NMHC)", "PT08.S5(O3)", "NOx(GT)", "PT08.S3(NOx)", "Unnamed: 15", "Unnamed: 16"])
          .dropna()
         # .assign(...)
      )

    #changing format to fit the graph
    df2['Temperature'] = df2['Temperature'].str.replace(',','.')
    df2['Temperature'] = df2['Temperature'].astype(float)
    df2['Benzene(GT)'] = df2['Benzene(GT)'].str.replace(',','.')
    df2['Benzene(GT)'] = df2['Benzene(GT)'].astype(float)
    df2['CO(GT)'] = df2['CO(GT)'].str.replace(',','.')
    df2['CO(GT)'] = df2['CO(GT)'].astype(float)
    df2['Relative Humidity'] = df2['Relative Humidity'].str.replace(',','.')
    df2['Relative Humidity'] = df2['Relative Humidity'].astype(float)
    df2['Absolute Humidity'] = df2['Absolute Humidity'].str.replace(',','.')
    df2['Absolute Humidity'] = df2['Absolute Humidity'].astype(float)
    # Make sure to return the latest dataframe
      


    return df2
