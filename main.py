from analysis.scripts import project_functions

df = project_functions.load_and_process("data\\raw\\AirQualityUCI.csv")

print(df.head())
