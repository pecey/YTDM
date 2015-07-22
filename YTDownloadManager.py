#!/usr/bin/env python3

import os
import sys
import argparse
import threading
import youtube_dl as yt

class Downloader(threading.Thread):
	def __init__(self, filename):
		threading.Thread.__init__(self)
		with open(filename,'r') as f:	
			self.urls = f.readlines()
	
	def run(self):
		for url in self.urls:
			#print("Downloading "+url)
			self.download(url)

	def download(self, url):
                #print("[+]Downloading "+url)
                opts = {'quiet':True, 'forcetitle':True}
	        with yt.YoutubeDL(opts) as yd:
			yd.download([url])


def updateManager(filename, url):
    try:
        with open(filename, 'a') as f:
           f.write(url)
        print("[+] "+url+" has been added to the manager and will be downloaded shortly")
    except:
        print("[-] There was some error processing your request!. Exiting.")
        sys.exit(0)
    


parser = argparse.ArgumentParser(description="This is a download manager for YouTube videos, using youtube-dl module")
parser.add_argument("-m","--manager",help="Enter the path for the filename where the download list is stored.", default="YTDownloader.txt")
parser.add_argument("-u","--url",help="Enter the download link, and add it to the file.")
args = parser.parse_args()
print(args)

#Check if filename is given for manager. If no filename, set it to default.
filename=args.manager
if(os.path.isfile(filename)):
    print("[+] Download list located. Proceeding to download.")
else:
    print("[-] Failed to locate the download list. Exiting.")
    sys.exit(0)

# Check if url is to be added to the manager.
if args.url:
    url = args.url
    updateManager(filename,url)

d=Downloader(filename)
d.start() 
		
	
