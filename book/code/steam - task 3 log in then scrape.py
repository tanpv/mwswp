from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')


def login(username, password):
	url = 'https://store.steampowered.com/'
	driver.get(url)
	
	# click login link
	driver.find_element_by_xpath('//*[@id="global_action_menu"]/a').click()

	# input user name
	driver.find_element_by_xpath('//*[@id="input_username"]').send_keys(username)

	# input password
	driver.find_element_by_xpath('//*[@id="input_password"]').send_keys(password)

	# click to button login
	driver.find_element_by_xpath('//*[@id="login_btn_signin"]/button').click()

	# sleep some time
	time.sleep(5)



def top_seller():

	# search web scraping
	url = 'https://store.steampowered.com/search/?filter=topsellers&os=win'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	# search for div contain all game
	div = soup.find('div', {'id':'search_result_container'})

	# search for a contain one game
	for a in div.find_all('a', class_='search_result_row'):

		# search for title
		span_name = a.find('span', class_='title')
		print(span_name.text)
		print(a['href'])

		# search for detail
		detail(a['href'])
		print('\n')


def detail(url):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	detail = soup.find('div', class_='game_area_description')
	if detail is not None:
		print(detail.text.replace('	',''))


login('your account', 'your password')
top_seller()

driver.close()
