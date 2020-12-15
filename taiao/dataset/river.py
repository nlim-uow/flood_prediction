import pandas as pd
data=pd.read_csv('filtered_2015_river_rain_accumulation.csv')
temp=data.iloc[:,2:]
timeSeries=temp.values
def x(mode,forecast_length):
    if mode=="train":
       val=timeSeries[0:403254,0:4]
    else:
       val=timeSeries[403255:576077-forecast_length,0:4]
    return val

def y(mode,forecast_length):
    if mode=="train":
       val=timeSeries[forecast_length:403254+forecast_length,0]
    else:
       val=timeSeries[403255+forecast_length:576077,0]
    return val