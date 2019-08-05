from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def get_movies():

	url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
	
	driver.get(url)

	soup = BeautifulSoup(driver.page_source,'lxml')

	table = soup.find('table', class_ = 'chart')

	for td in table.find_all('td', class_ = 'titleColumn'):
		
		full_title = td.text.strip().replace('\n','').replace('      ','')
		# print(full_title)

		rank = full_title.split('.')[0]
		print('rank   : ', rank)

		title = full_title.split('.')[1].split('(')[0]
		print('titele : ', title)

		year = full_title.split('(')[1][:-1]
		print('year   : ', year)

		a = td.find('a')
		print('link   : ', a['href'])

		print('\n')

get_movies()

driver.quit()
