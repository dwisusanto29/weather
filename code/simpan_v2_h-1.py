import pandas as pd
import sys
from sqlalchemy import create_engine
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=1)
name = d.strftime("%Y%m%d")

#filename = "/home/pi/DataArduino/data/data"+name+".csv"
filename = "/home/pi/DataArduino/weather/data/a"+name+".csv"
#filename = sys.argv[1]
#fileout = filename[3:]
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
data = pd.read_csv(filename, sep=",",  skiprows=1, names=['waktu', 'tanggal', 'derajat_arah_angin', 'kecepatan_angin_avg', 'kecepatan_angin_max', 'hujan_jam','hujan_hari','suhu', 'kelembaban','tekanan_udara'], date_parser=dateparse, index_col=0) 
#dataku = data.asfreq('2Min', method='pad')

engine = create_engine('mysql+pymysql://alvin:alvin@202.124.205.201:3306/db_dws', echo=False)
data.to_sql(name='tb_pengamatan', con=engine, if_exists = 'append', index=True)
