import subprocess
from random import shuffle
import re

# A requirement for this program is to have omxplayer installed, do this by calling
# sudo apt-get install omxplayer on a debian based system.

def play(what):
   final_string = "-o hdmi " + what
   subprocess.call("omxplayer " + final_string,shell=True)

def parseRSS(url):
   print "Pull out all URL's from RSS FEED" 
   returnList = []
   subprocess.call("wget -O rssplayerTemp.html " + url, shell=True)
   f = open("rssplayerTemp.html", 'r')
   for line in f:
        m = re.search('media:content url=\"(.*?)\" ',line)
        if m:
           returnList.append(m.group(1))
   f.close()
   return returnList
   #<media:content url="http://download.ted.com/talks/KeithChen_2012G-480p.mp4?apikey=172BB350-0206" fileSize="87761380" type="video/mp4" />
   
while 1==1:
   listOfVideos = parseRSS("http://feeds.feedburner.com/tedtalkshd")

   shuffle(listOfVideos)

   for link in listOfVideos:
      play(link)


