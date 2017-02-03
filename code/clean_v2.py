
import pandas as pd
import sys
from datetime import datetime

from datetime import datetime, timedelta

d = datetime.today()
name = d.strftime("%Y%m%d")

filename = "/home/pi/DataArduino/data/data"+name+".csv"
fileout = "/home/pi/DataArduino/weather/data/a"+name+".csv"

data = pd.read_csv(filename, sep=",",  skiprows=1, names=['waktu', 'tanggal', 'winddir', 'windspeed1', 'windspeed2', 'Rain1','Rain2','temperature', 'humidity','Pressure'], low_memory=False) 

satu = data[data.tanggal < '0000-00-00']
dua = satu[satu.humidity > 0]
baru = dua.dropna(axis=0)
dataku = baru.drop_duplicates(['waktu'])
dataku.to_csv(fileout, sep=',', encoding='utf-8', index=False, header=False)



