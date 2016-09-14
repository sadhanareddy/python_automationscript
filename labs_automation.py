from bs4 import BeautifulSoup
import urllib2
import urlparse
import sys
import requests
import json

def fetch_urls_of_homepage(base_url):
	url_list_with_http = []
	url_list_without_http = []
	html = urllib2.urlopen(base_url)
	soup = BeautifulSoup(html)
	#print soup.prettify()
	soup.header.decompose()
	soup.footer.decompose()
	soup.head.decompose()
	soup.h2.decompose()
	# print soup.prettify()
	for link in soup.find_all('a'):
		# print link
		#print link.get('href')
		pagelinks = str(link.get('href'))
		#print pagelinks
		if pagelinks.startswith('http'):
			url_list_with_http.append(pagelinks)
		else : 
			url_list_without_http.append(urlparse.urljoin(base_url, pagelinks))
			#print url_list_without_http
	return url_list_without_http	

#sections_fileslist = ["Introduction", "List of Experiments", "Target audience", "Courses Aligned", "Prerequisites", "Feedback"]

def fetch_homepage_content(final_list):
	for section_link in range(len(final_list)):
		# print section_link
		html = requests.get(final_list[section_link])
		# print html
		soup = BeautifulSoup(html.content)                                                                                                      
		# print soup.prettify()
		sectioncontent = str(soup.h1.next_sibling)
		#print sectioncontent
		labspec = json.loads(open('labspec.json', 'r').read())
		# print labspec
		filename = labspec['experiments'][0]['subsections'][section_link]['name'] + '.html'
		# print filename
		file = open(filename, 'w')
		# print file

		# if section_link == final_list[0]:
		# 	filename = sections_fileslist[0] + '.html'
		# 	# print filename
		# 	file = open(filename, 'w')

		try:
			file.write(sectioncontent)
			file.close()
			# break	
		except Exception as e:
			print str(e)

		
def fetch_urls_of_exptpage(url):
	expt_list_with_http = []
	expt_list_without_http = []
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)
	soup.header.decompose()
	soup.footer.decompose()
	soup.head.decompose()
	soup.h2.decompose()
	soup.find('div',class_='col-md-2 sidebar-col-2').decompose()
	# print soup.prettify()
	for link in soup.find_all('a'):
		# print link
		print link.get('href')
	# 	pagelinks = str(link.get('href'))
	# 	#print pagelinks
	# 	if pagelinks.startswith('http'):
	# 		expt_list_with_http.append(pagelinks)
	# 	else : 
	# 		expt_list_without_http.append(urlparse.urljoin(url, pagelinks))
	# #print expt_list_without_http
	# return expt_list_without_http
	

# def fetch_expt_sections_ashay(url):
# 	list_with_http = []
# 	list_without_http = []
# 	html = urllib2.urlopen(url)
# 	soup = BeautifulSoup(html) 
# 	soup.header.decompose()
# 	soup.footer.decompose()
# 	soup.head.decompose()
# 	soup.find('a',class_='sidebar-a').decompose()
# 	for section in soup.find_all('a'):
# 		pagelinks = str(section.get('href'))
# 		if pagelinks.startswith('http'):
# 			list_with_http.append(pagelinks)
# 		else : 
# 			list_without_http.append(urlparse.urljoin(sectionlink, pagelinks))
# 	        # return list_without_http
# 	        print list_without_http


# 	# for section_link in experiment_links:
# 	# 	html = urllib2.urlopen(section_link)
# 	# 	soup = Beautifulsoup(html)
# 	# 	section_content = soup.find_next_siblings(tagname)
# 	# 	filename = sectionname + '.html'
# 	# 	openfile = open(filename, 'w')
# 	# 	openfile.close()
# 	# 	break


lab_url = "http://cse14-iiith.vlabs.ac.in/"
final_list = fetch_urls_of_homepage(lab_url) 
#print final_list

fetch_homepage_content(final_list)
# fetch_homepage_content(final_list,  "List of Experiments")
# fetch_homepage_content(final_list,  "Target Audience")
# fetch_homepage_content(final_list,  "Courses Aligned")
# fetch_homepage_content(final_list,  "Prerequisites")
# fetch_homepage_content(final_list,  "Feedback")


expt_url = "http://cse14-iiith.vlabs.ac.in/List%20of%20experiments.html?domain=Computer%20Science"
experiment_links = fetch_urls_of_exptpage(expt_url)
# print experiment_links

# for sectionlink in experiment_links:
# 	fetch_expt_sections_ashay(sectionlink)

#fetch_expt_sections(experiment_links)
# fetch_expt_page_content(experiment_links, h1, "Theory")











