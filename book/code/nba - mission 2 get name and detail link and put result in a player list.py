from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')

def get_all_name_and_detail_link():
	url = 'https://stats.nba.com/players/list/'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_= 'stats-player-list')

	players = []

	for li in div.find_all('li', class_='players-list__name'):
		player = {}
		player['link'] = li.find('a')['href']
		player['name'] = li.text
	
		players.append(player)

		print(player['name'])
		print(player['link'])
		print('\n')
	
	return players

get_all_name_and_detail_link()

driver.quit()
