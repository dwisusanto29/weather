<?php
	$host = "202.124.205.201";
	$user = "alvin";
	$pass = "alvin";
	$db = "db_dws";
	mysql_connect($host, $user, $pass);
	mysql_select_db($db);

	$namafile = $argv[1];
	$file = fopen($namafile,"r");

	while($data = fgetcsv($file) !== false){
		if (array(null) !== $data) { 
			$now = $data[0];
			$tgl = $data[1];
			$win_dir = $data[2];
			$winds_avg = $data[3];
			$winds_max = $data[4];
			$rain_h = $data[5];
			$rain_d = $data[6];
			$temp = $data[7];
			$hum = $data[8];
			$press = $data[9];
			$query = "INSERT INTO tb_pengamatan(waktu, tanggal, location, suhu, kelembaban, tekanan_udara, kecepatan_angin_avg, kecepatan_angin_max, derajat_arah_angin, hujan_jam, hujan_hari) VALUES('$now', '$tgl', 4, $temp, $hum, $press, $winds_avg, $winds_max, $wind_dir, $rain_h, $rain_d)";
			mysql_query($query);

		}
	}
	
	
?>