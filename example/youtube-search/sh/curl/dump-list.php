#!/usr/bin/env php
<?php

	$input = file_get_contents("php://stdin");

	$data = json_decode($input, true);

	$list = $data['items'];

	//var_dump($list);

	foreach ($list as $key => $item) {
		//var_dump($item);
		$id = $item['id']['videoId'];
		echo 'id: ' . $id . PHP_EOL;
		echo 'title: ' . $item['snippet']['title'] . PHP_EOL;
		echo 'mpv_play_command_1: ' . 'mpv ytdl://' . $id . PHP_EOL;
		echo 'mpv_play_command_2: ' . 'mpv --cache-secs=600 ytdl://' . $id . PHP_EOL;
		echo 'mpv_play_command_3: ' . "mpv 'https://www.youtube.com/watch?v=" . $id . "'" . PHP_EOL;
		echo 'firefox_view_command: ' . "firefox 'https://www.youtube.com/watch?v=" . $id . "'" . PHP_EOL;
		echo 'youtube_dl_download_command_1: ' . "youtube-dl 'https://www.youtube.com/watch?v=" . $id . "'" . PHP_EOL;
		echo 'youtube_dl_download_command_2: ' . "youtube-dl '" . $id . "'" . PHP_EOL;
		echo PHP_EOL;
	}
