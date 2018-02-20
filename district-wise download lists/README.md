URL lists split by district.

Download usind `aria2c` command. Get it here: <https://aria2.github.io>

Usage:
```
aria2c -x10 -j10 -k1M -c -i <district>-pdfs.txt
```

* -x10 : set max connections per server to 10 (feel free to experiment with this depending on your connection and host site)
* -j10 : set concurrent downloads to 10
* -k1M : set download split / chunk size to 1 MB.
* -c : resume broken downloads in case the download was interrupted earlier 
* -i : specify a file having list of URLs to download.

In case the juiced up parallel download settings aren't working out for you, here's a simplified command that runs on default settings:
```
aria2c -c -i <district>-pdfs.txt
```
