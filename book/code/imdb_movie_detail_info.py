from bs4 import BeautifulSoup
from selenium import  webdriver
import requests

driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')

def get_movies():
	url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	table = soup.find('table', class_='chart')

	for td in table.find_all('td', class_='titleColumn'):
		full_title = td.text.replace('\n','').replace('      ','')

		rank = full_title.split('.')[0]
		print(rank)

		title = full_title.split('.')[1].split('(')[0]
		print(title)

		year = full_title.split('(')[1][:-1]
		print(year)

		a = td.find('a')
		print(a['href'])

		detail_link = 'https://www.imdb.com' + a['href']
		
		large_poster_link = 'https://www.imdb.com' + get_large_poster_link(detail_link)

		download_large_poster(large_poster_link, title)

		print('\n')

def get_large_poster_link(detail_link):
	driver.get(detail_link)
	soup = BeautifulSoup(driver.page_source,'lxml')
	div = soup.find('div', class_='poster')
	a = div.find('a')
	print(a['href'])
	return a['href']

def download_large_poster(large_poster_link, title):
	driver.get(large_poster_link)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_='pswp__zoom-wrap')
	img = div.find_all('img')[1]
	print(img['src'])

	f = open('imdb_posters/{0}.jpg'.format(title), 'wb')
	f.write(requests.get(img['src']).content)
	f.close()

get_movies()
driver.quit()