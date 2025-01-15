import pandas as pd

# MAKING A DATA ARRAY FROM THE CSV FILE:
dataset = pd.read_csv('rdu-weather-history.csv', sep=",")

# GENERAL STATS ABOUT THE DATASET
print("\n\nWEATHER ANALYSIS - CARY, NORTH CAROLINA\n")
print("NUMBER OF DATAPOINTS         :", dataset.Date.count())
print("FIRST MEASUREMENT DATE       :", dataset.Date[0])
print("LAST MEASUREMENT DATE        :", dataset.Date.iloc[-1])
print("\n")
print("AVERAGE MINIMUM TEMPERATURE  :", dataset.TemperatureMinimum.mean(), "F")
print("AVERAGE MAXIMUM TEMPERATURE  :", dataset.TemperatureMaximum.mean(), "F")
print("AVERAGE MIN-MAX MEAN         :", (dataset.TemperatureMinimum.mean() + dataset.TemperatureMaximum.mean())/2, "F")
print("HIGHEST RECORDED TEMPERATURE :", dataset.TemperatureMaximum.max(), "F on", dataset.Date[dataset["TemperatureMaximum"].idxmax()])
print("LOWEST RECORDED TEMPERATURE  :", dataset.TemperatureMinimum.min(), "F on", dataset.Date[dataset["TemperatureMinimum"].idxmin()])
print("\n")
print("AVERAGE MINIMUM SNOWFALL     :", dataset.Snowfall.mean(), "Inches")
print("HIGHEST RECORDED SNOWFALL    :", dataset.Snowfall.max(), "inches on", dataset.Date[dataset["Snowfall"].idxmax()])
print("LOWEST RECORDED SNOWFALL     :", dataset.Snowfall.min(), "inches on", dataset.Date[dataset["Snowfall"].idxmin()])
print("AVERAGE SNOW DEPTH           :", dataset.SnowDepth.mean())
print("HIGHEST RECORDED SNOW DEPTH  :", dataset.SnowDepth.max(), "inches on", dataset.Date[dataset["SnowDepth"].idxmax()])
print("LOWEST RECORDED SNOW DEPTH   :", dataset.SnowDepth.min(), "inches on", dataset.Date[dataset["SnowDepth"].idxmin()])
print("\n")
print("AVERAGE WIND SPEEDS          :", dataset.AverageWindSpeed.mean())
print("HIGHEST RECORDED AVG. WINDS  :", dataset.AverageWindSpeed.max(), "mph on", dataset.Date[dataset["AverageWindSpeed"].idxmax()])
print("LOWEST RECORDED AVG. WINDS   :", dataset.AverageWindSpeed.min(), "mph on", dataset.Date[dataset["AverageWindSpeed"].idxmin()])