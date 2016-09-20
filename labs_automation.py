from bs4 import BeautifulSoup
import urllib2
import urlparse
import os, sys
import requests
import json


def fetch_urls_of_homepage(base_url):
	url_list_with_http = []
	url_list_without_http = []
	html = urllib2.urlopen(base_url)
	soup = BeautifulSoup(html)
	soup.header.decompose()
	soup.footer.decompose()
	soup.head.decompose()
	# print soup.prettify()
	for link in soup.find_all('a'):
		pagelinks = str(link.get('href'))
		# print pagelinks
		if pagelinks.startswith('http'):
			url_list_with_http.append(pagelinks)
		else : 
			url_list_without_http.append(urlparse.urljoin(base_url, pagelinks))
	return url_list_without_http	

#sections_fileslist = ["Introduction", "List of Experiments", "Target audience", "Courses Aligned", "Prerequisites", "Feedback"]

def fetch_homepage_content(final_list):
	for section_link in range(len(final_list)):
		html = requests.get(final_list[section_link])
		soup = BeautifulSoup(html.content)                                                                                                      
		sectioncontent = str(soup.h1.next_sibling)
		labspec = json.loads(open('labspec.json', 'r').read())
		filename = labspec['experiments'][0]['subsections'][section_link]['name'] + '.html'
		file = open(filename, 'w')
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
	soup.find('div',class_='col-md-2 sidebar-col-2').decompose()
	# print soup.prettify()
	for link in soup.find_all('a'):
		pagelinks = str(link.get('href'))
		if pagelinks.startswith('http'):
			expt_list_with_http.append(pagelinks)
		else : 
			expt_list_without_http.append(urlparse.urljoin(url, pagelinks))
	# print expt_list_without_http
	return expt_list_without_http
	

def fetch_expt_sections_links(url):
	list_with_http = []
	list_without_http = []
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html) 
	soup.header.decompose()
	soup.footer.decompose()
	soup.head.decompose()
	# soup.find('a',class_='sidebar-a').decompose()
	soup.h2.decompose()
	for section in soup.find_all('a'):
		pagelinks = str(section.get('href'))
		if pagelinks.startswith('http'):
			list_with_http.append(pagelinks)
		else: 
			list_without_http.append(urlparse.urljoin(experiment_links[sectionlink], pagelinks))
			# print list_without_http
	return list_without_http
	        
def fetch_exptspage_content(explinks):
	# dir_name =  "expt" + str(sectionlink)
	# os.mkdir(dir_name)
	for section_link in range(len(explinks)):
		html = requests.get(explinks[section_link])
		soup = BeautifulSoup(html.content)
		# soup.find_all('img').get('src') = urlparse.urljoin(explinks[section_link], image_src)
		for img_tag in soup.find_all('img'):
			image_src = str(img_tag.get('src'))
		
			tag = urlparse.urljoin(explinks[section_link], image_src)
			print tag
		# 	soup.find('img')['src'] = tag
		# 	print soup.find('img')['src']
		# 	print soup
		# 	image_src.replace_with(tag)
			# print soup
			# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
			# soup = BeautifulSoup(markup)
			# a_tag = soup.find_all('img')

			# new_tag = soup.new_tag("b")
			# new_tag.string = "example.net"
			# image_src.replace_with(tag)
			# print image_src.replace_with(tag)
		soup = BeautifulSoup(html.content)	
		sectioncontent = str(soup.h1.next_sibling)
		labspec = json.loads(open('labspec.json', 'r').read())
		filename1 = labspec['experiments'][i]['name']+"_"+labspec['experiments'][section_link + 1]['subsections'][section_link]['name']+ "_"+"Unit"+"_"+"html"+'.html'
		filename = filename1.replace(" ","_")
		# filename = labspec['experiments'][section_link + 1]['subsections'][section_link]['name'] + '.html'
		# file = open(os.path.join(dir_name, filename), 'w')
		file = open(filename, 'w')
		try:
			file.write(sectioncontent)
			file.close()
			# break	
		except Exception as e:
			print str(e)


lab_url = "http://sd-iiith.vlabs.ac.in/"
final_list = fetch_urls_of_homepage(lab_url) 
# print final_list

fetch_homepage_content(final_list)


expt_url = "http://sd-iiith.vlabs.ac.in/List%20of%20experiments.html?domain=Civil%20Engineering"
experiment_links = fetch_urls_of_exptpage(expt_url)
# print experiment_links
i = 0
for sectionlink in range(len(experiment_links)):
	i = i+1
	explinks = fetch_expt_sections_links( experiment_links[sectionlink])
	# print explinks
	fetch_exptspage_content(explinks)
	












