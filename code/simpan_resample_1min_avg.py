import pandas as pd
import sys
from sqlalchemy import create_engine

filename = sys.argv[1]
#fileout = sys.argv[2]
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
data = pd.read_csv(filename, sep=",",  skiprows=1, names=['waktu','tanggal', 'derajat_arah_angin', 'kecepatan_angin_avg', 'kecepatan_angin_max', 'hujan_jam','hujan_hari','suhu', 'kelembaban','tekanan_udara'], date_parser=dateparse, index_col=0, low_memory=True) 
#satu = data[data.tanggal < '0000-00-00']
#data['tanggal']= data[data[:10]]
data['lokasi']='4'
dataku = data.resample('1Min').mean()
baru = dataku.dropna()
engine = create_engine('mysql+pymysql://alvin:alvin@202.124.205.201:3306/db_dws_baru', echo=False)
baru.to_sql(name='tb_pengamatan', con=engine, if_exists = 'append', index=True)
#data.to_csv(fileout, sep=',', encoding='utf-8', index=True, header=False)

