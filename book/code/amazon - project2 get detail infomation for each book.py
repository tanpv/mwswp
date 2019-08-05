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

		detail_link = 'https://www.amazon.com' + a['href']
		get_detail(detail_link)

		print('\n')


def get_detail(url):
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')
	
	# get isbn
	table = soup.find('table', {'id':'productDetailsTable'})
	all_li = table.find_all('li')
	isbn = all_li[3].text.replace('ISBN-10:','')
	print('isbn : ', isbn)

	# get description
	driver.switch_to.frame(driver.find_element_by_id('bookDesc_iframe'))
	soup = BeautifulSoup(driver.page_source,'lxml')
	description = soup.find('div')
	print('description : ', description.text)

get_book_list()

driver.quit()
