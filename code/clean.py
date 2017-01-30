
import pandas as pd
import sys

filename = sys.argv[1]
fileout = "/home/pi/DataArduino/weather/"+filename[-13:]
data = pd.read_csv(filename, sep=",",  skiprows=1, names=['waktu', 'tanggal', 'winddir', 'windspeed1', 'windspeed2', 'Rain1','Rain2','temperature', 'humidity','Pressure'], low_memory=False) 

satu = data[data.humidity > 0]
baru = satu.dropna(axis=0)
dataku = baru.drop_duplicates(['waktu'])
dataku.to_csv(fileout, sep=',', encoding='utf-8', index=False, header=False)


