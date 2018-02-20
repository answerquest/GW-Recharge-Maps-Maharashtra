URL lists split by district.

Download usind `aria2c` command. Get it here: <https://aria2.github.io>

Usage:
```
aria2c -x10 -j10 -k1M -c -i <district>-pdfs.txt
```

* -x10 : set max connections per server to 10
* -j10 : set concurrent downloads to 10
* -k1M : set download split / chunk size to 1 MB.
* -c : continue 
* -i : specify a file having list of URLs to download.

In case the parallel dload settings aren't working out for you, here's a simplified command:
```
aria2c -c -i <district>-pdfs.txt
```
