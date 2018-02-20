# GW-Recharge-Maps-Maharashtra
Script and links list for downloading Ground Water Recharge Priority maps of individual villages in Maharashtra from GSDA site, <https://gsda.maharashtra.gov.in/english/index.php/GWRechargePriorityMap>

### Usage:
```
python3 gsda.py
```

The program loops through villages.json (which is put together from JSON responses recieved on above page in browser developer pane). It creates district-wise download lists which have the source URL and the destination filename, in the format used by the popular `aria2` downloader. It can be downloaded here: <https://aria2.github.io>

### Output:
```
$ python3 gsda.py 
Created Aurangabad-pdfs.txt
Created Jalna-pdfs.txt
Created Parbhani-pdfs.txt
Created Latur-pdfs.txt
Created Hingoli-pdfs.txt
Created Osmanabad-pdfs.txt
Created Beed-pdfs.txt
Created Nanded-pdfs.txt
Created Jalgaon-pdfs.txt
Created Nashik-pdfs.txt
Created Ahmednagar-pdfs.txt
Created Dhule-pdfs.txt
Created Nandurbar-pdfs.txt
Created Kolhapur-pdfs.txt
Created Pune-pdfs.txt
Created Solapur-pdfs.txt
Created Sangali-pdfs.txt
Created Satara-pdfs.txt
Created Yevatmal-pdfs.txt
Created Buldana-pdfs.txt
Created Akola-pdfs.txt
Created Washim-pdfs.txt
Created Amravati-pdfs.txt
Created Gondia-pdfs.txt
Created Gadchiroli-pdfs.txt
Created Chandrapur-pdfs.txt
Created Bhandara-pdfs.txt
Created Wardha-pdfs.txt
Created Nagpur-pdfs.txt
Created Palghar-pdfs.txt
Created Sindhudurg-pdfs.txt
Created Ratnagiri-pdfs.txt
Created Raigad-pdfs.txt
Created Thane-pdfs.txt
Run this command to download: aria2c -x10 -j10 -k1M -c -i <district>-pdfs.txt
```

The district-wise lists are stored in a folder on this repo.
