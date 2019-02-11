
## Test

> Please replace [main.sh / {YOUR_API_KEY}] first!

Then

run

``` sh
$ ./main.sh
```

run

``` sh
$ ./main.sh | php -r '$input = file_get_contents("php://stdin"); var_dump(json_decode($input, true));' | less
```

* http://php.net/manual/en/function.file-get-contents.php#110297
* http://php.net/manual/en/features.commandline.io-streams.php
* http://php.net/manual/en/function.json-decode.php


run

``` sh
$ ./main.sh | ./dump-json.php | less
```

run

``` sh
$ ./main.sh | ./dump-list.php | less
```


## Reference

* https://developers.google.com/youtube/v3/docs/#calling-the-api
* https://developers.google.com/youtube/v3/docs/search/list
* https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.search.list?q=surfing&maxResults=25&part=snippet
* https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools


## Reference Project


### youtube-search-provider

* https://www.atareao.es/aplicacion/videos-de-youtube-en-ubuntu/
* https://gitlab.gnome.org/atareao/youtube-search-provider
* https://gitlab.gnome.org/atareao/youtube-search-provider/blob/master/youtube_client.js#L155


### youtube-viewer

* https://trizenx.blogspot.com/2012/03/gtk-youtube-viewer.html
* https://github.com/trizen/youtube-viewer
* https://github.com/trizen/youtube-viewer/blob/master/bin/gtk-youtube-viewer#L730
* https://github.com/trizen/youtube-viewer/blob/master/bin/gtk-youtube-viewer#L2222
* https://github.com/trizen/youtube-viewer/blob/master/bin/youtube-viewer#L608
* https://github.com/trizen/youtube-viewer/blob/master/bin/youtube-viewer#L1223
* https://github.com/trizen/youtube-viewer/blob/master/lib/WWW/YoutubeViewer.pm#L164
* https://github.com/trizen/youtube-viewer/blob/master/lib/WWW/YoutubeViewer.pm#L477
* https://github.com/trizen/youtube-viewer/blob/master/lib/WWW/YoutubeViewer/Search.pm#L79
* https://github.com/trizen/youtube-viewer/blob/master/lib/WWW/YoutubeViewer/Search.pm#L24
* https://github.com/trizen/youtube-viewer/blob/master/lib/WWW/YoutubeViewer.pm#L490
* ~/.config/youtube-viewer/youtube-viewer.conf        (let [debug => 2,])
* ~/.config/youtube-viewer/gtk-youtube-viewer.conf    (let [debug => 2,])
