#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import re
import hashlib
from datetime import datetime
import requests
import cfscrape
import random
from guessit import guessit
import getpass

class Elite_Tracker:

	cookies = ""
	scraper = cfscrape.create_scraper()
	
	
	def __init__(self,_cookies):
		self.cookies=_cookies
		
	def __init__(self):
		self.cookies=""		
	
	def download_torrent(self, _torrent):
		try:
			file_torrent = self.scraper.get(_torrent, cookies=self.cookies).content 
		except IOError:
			erreur=1	
			
		with open(_torrent.split("https://elite-tracker.net/")[1]+".torrent",'wb') as output:
			output.write(file_torrent)				
	
	def login(self):		
		pseudo = getpass.getpass('Pseudo > ')
		password = getpass.getpass('Password > ')

		try:
			r = self.scraper.post("https://elite-tracker.net/takelogin.php", data = {'username': pseudo, 'password': password}) 
		except IOError:
			erreur=1		
	
		safe_username = self.scraper.cookies['c_secure_uid']
		safe_password = self.scraper.cookies['c_secure_pass']
		
		self.cookies = dict(c_secure_uid=safe_username, c_secure_pass=safe_password)
	
	def search_torrent(self,_search):
		rand = random.randint(1,1000)
		erreur=0
		
		cookie_valide = False
		for i in range (0,2):
			try:
				codeSrc = self.scraper.post("https://elite-tracker.net/browse.php", data = {'searchtorrent': '1', 'keywords':_search, 'do' : 'search', 'search_type': 't_name', 'category': 48, 'include_dead_torrents': 0, 'Recherche': 1}, cookies=self.cookies).content 
			except IOError:
				erreur=1			
				
			try:			
				codeSrc = codeSrc.split('<script type="text/javascript" src="https://elite-tracker.net/scripts/ts_update.js?v=7.2"></script>')[1]
			except IndexError:
				cookie_valide = False
			else:
				cookie_valide = True

			if not cookie_valide:				
				r=self.login()
			
					
		links = re.findall('https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+](?!c)(?!u[0-9])|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F] ))+[0-9]\.ts', codeSrc)
		final_link=[]
		
		for link in links:
			if link.find("-s-") != -1:
				continue
			
			name = guessit(link.split("https://elite-tracker.net/")[1])
			format_s = ""
			
			if name.has_key("title"):
				format_s = format_s+str(name['title'])+" "
			if name.has_key("year"):
				format_s = format_s+str(name['year'])+" "			
			if name.has_key("screen_size"):
				format_s = format_s+str(name['screen_size'])+" "
			if name.has_key("language"):
				format_s = format_s+str(name['language'])+" "
			if name.has_key("other"):
				format_s = format_s+str(name['other'])+" "
			if name.has_key("audio_codec"):
				format_s = format_s+str(name['audio_codec'])+" "
			if name.has_key("video_codec"):
				format_s = format_s+str(name['video_codec'])+" "	
			final_link.append([link,format_s])
		return final_link