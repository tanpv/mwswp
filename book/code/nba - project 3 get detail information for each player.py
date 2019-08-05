from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')

def get_all_name_and_detail_link():
	url = 'https://stats.nba.com/players/list/'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_='stats-player-list')

	players = []

	for li in div.find_all('li', class_='players-list__name')[:20]:
		player = {}
		player['name'] = li.text
		player['link'] = 'https://stats.gleague.nba.com' + li.find('a')['href']
		
		stat = get_detail_info_for_one_player(player['link'])
		player['stat'] = stat

		print('name : ', player['name'])
		print('link : ',player['link'])
		print('pts : ', stat['pts'])
		print('reb : ', stat['reb'])
		print('ast : ', stat['ast'])
		print('pie : ', stat['pie'])

		print('\n')

		players.append(player)
	
	return players


def get_detail_info_for_one_player(url):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_='player-stats')

	div_pts = div.find('div', class_='player-stats__pts')
	div_reb = div.find('div', class_='player-stats__reb')
	div_ast = div.find('div', class_='player-stats__ast')
	div_pie = div.find('div', class_='player-stats__pie')

	stat = {}
	stat['pts'] = div_pts.text.replace('PTS','').replace('\n','')
	stat['reb'] = div_reb.text.replace('REB','').replace('\n','')
	stat['ast'] = div_ast.text.replace('AST','').replace('\n','')
	stat['pie'] = div_pie.text.replace('PIE','').replace('\n','')

	return stat


get_all_name_and_detail_link()

driver.quit()
