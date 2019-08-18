from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def get_book_list():
	url = 'https://www.amazon.com/s?k=python+programming'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_='s-result-list')

	for a in div.find_all('a', class_ = 'a-link-normal a-text-normal'):
		print('title : ',a.text.replace('\n', ''))
		print('link : ', a['href'])
		print('\n')
		print('\n')

get_book_list()

driver.close()