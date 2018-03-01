# EliteTracker-Python
EliteTracker Class in python 2.7 to search and download any torrents (French Tracker)

## Usage

### Simple download

`python2 elite-download.py avatar`

### Auto downloading first item:

`python2 elite-download.py "Edge of tomorrow" --first`


## Class

### Auth with cookie:

`cookies = dict(c_secure_uid='YOUR_UID', c_secure_pass='YOUR_SECURE_PASS')`

`x = Elite_Tracker(cookies)`

### Getting search result:

`result = x.search_torrent("Avatar")`

### Downloading torrent:

`x.download_torrent(URL)`
