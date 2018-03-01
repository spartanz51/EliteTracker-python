# EliteTracker-Python
EliteTracker Class in python 2.7 to search and download any torrents (French Tracker)

# Auth with cookie

cookies = dict(c_secure_uid='YOUR_UID', c_secure_pass='YOUR_SECURE_PASS')

x = Elite_Tracker(cookies)

# Getting search result
result = x.search_torrent("Avatar")
