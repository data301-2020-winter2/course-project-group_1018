import csv
with open("data\\raw\\AirQualityUCI.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(row["Date"]+":"+row["Time"]+row["CO(GT)"])