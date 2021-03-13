import pandas as pd 
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file, delimiter=";")
          .rename(
              columns={"PT08.S4(NO2)":"Tungsten Oxide(NO2, S4)", "PT08.S1(CO)":"Tin Oxide (CO, S1)", "C6H6(GT)":"Benzene(GT)", "NO2(GT)":"NO2(GT)", "T": "Temperature", "RH":"Relative Humidity", "AH":"Absolute Humidity", "Time":"Hour of Day", "NOx(GT)":"NOx(GT)", "PT08.S3(NOx)":"Tungsten Oxide(NOx, S3)", "NMHC(GT)":"Non Metal HydroCarbon (GT)", "PT08.S2(NMHC)":"Titania (NMHC, S2)", "PT08.S5(O3)":"Indium Oxide (O3, S5)"}
              )
      )
    # Method Chain 2 (Create new columns, drop others, and do processing)
    #changing format to fit the graph
    df1['Temperature'] = df1['Temperature'].str.replace(',','.')
    df1['Temperature'] = df1['Temperature'].astype(float)
    df1['Benzene(GT)'] = df1['Benzene(GT)'].str.replace(',','.')
    df1['Benzene(GT)'] = df1['Benzene(GT)'].astype(float)
    df1['CO(GT)'] = df1['CO(GT)'].str.replace(',','.')
    df1['CO(GT)'] = df1['CO(GT)'].astype(float)
    df1['Relative Humidity'] = df1['Relative Humidity'].str.replace(',','.')
    df1['Relative Humidity'] = df1['Relative Humidity'].astype(float)
    df1['Absolute Humidity'] = df1['Absolute Humidity'].str.replace(',','.')
    df1['Absolute Humidity'] = df1['Absolute Humidity'].astype(float)
    #df1['PT08.S3(NOx)'] = df1['PT08.S3(NOx)'].str.replace(',','.')
    #df1['PT08.S3(NOx)'] = df1['PT08.S3(NOx)'].astype(float)
    #df1['NOx(GT)'] = df1['NOx(GT)'].str.replace(',','.')
    #df1['NOx(GT)'] = df1['NOx(GT)'].astype(float)

    df2 = (
          df1
          .drop(columns=[  "Unnamed: 15", "Unnamed: 16"])
          .replace(-200, np.nan)
          .dropna()
         # .assign(...)
      )


    # Make sure to return the latest dataframe
      


    return df2
