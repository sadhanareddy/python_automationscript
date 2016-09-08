#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import requests
import urlparse

lab = 'http://cse14-iiith.vlabs.ac.in/'
page = urllib2.urlopen(lab)
soup = BeautifulSoup(page)
urllist = []
pagecontent = []

for link in soup.find_all('a')[7:12]:
   pagelinks = link.get('href')
   subsection_url =  urlparse.urljoin(lab, pagelinks)
   urllist.append(subsection_url)
   print urllist

#for i in range(len(urllist)):
   # file = urllib2.urlopen(urllist[i])
    #soup1 = BeautifulSoup(file)
   # print soup1
