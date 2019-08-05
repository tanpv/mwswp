from selenium import webdriver
from bs4 import BeautifulSoup

def get_all_name():
	url = 'https://stats.nba.com/players/list/'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_= 'stats-player-list')

	for li in div.find_all('li', class_='players-list__name'):
		print(li.text)

driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')

get_all_name()

driver.quit()