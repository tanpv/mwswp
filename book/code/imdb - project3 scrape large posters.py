from bs4 import BeautifulSoup
from selenium import webdriver
import requests

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def get_movies():

	url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source,'lxml')
	table = soup.find('table', class_ = 'chart')

	for td in table.find_all('td', class_ = 'titleColumn'):
		full_title = td.text.strip().replace('\n','').replace('      ','')

		rank = full_title.split('.')[0]
		print('rank   : ', rank)

		title = full_title.split('.')[1].split('(')[0]
		print('titele : ', title)

		year = full_title.split('(')[1][:-1]
		print('year   : ', year)

		a = td.find('a')
		print('link   : ', a['href'])

		detail_link = 'https://www.imdb.com' + a['href']
		large_poster_link = 'https://www.imdb.com' + get_large_poster_link(detail_link)
		download_large_poster(large_poster_link, title)

		print('\n')


def get_large_poster_link(url):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_='poster')
	a = div.find('a')
	print(a['href'])
	return a['href']


def download_large_poster(url, title):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	
	# get bigger poster
	img = soup.find_all('img', class_='pswp__img')[1]
	print(img['src'])

	# download
	f = open('imdb_posters/{0}.jpg'.format(title), 'wb')
	f.write(requests.get(img['src']).content)
	f.close()


get_movies()

driver.quit()


