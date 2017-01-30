
python /home/pi/DataArduino/data/clean.py /home/pi/DataArduino/data/"data"$(date +%Y%m%d".csv")
sleep 1s
python /home/pi/DataArduino/weather/code/simpan_v2.py /home/pi/DataArduino/weather/"a"$(date +%Y%m%d".csv")
sleep 1s
/home/pi/DataArduino/weather/code/commit.sh
