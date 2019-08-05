from selenium import webdriver
from bs4 import BeautifulSoup
import requests


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
		download_image_one_player(player['name'], player['link'])
		


def download_image_one_player(name, url):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div_img = soup.find('div', class_='player-summary__image-block')
	img = div_img.find('img')

	if 'gleague-logoman-fallback.png' not in img['src']:
		print('downloading {0} image '.format(name))
		f = open('nba_player/{0}.png'.format(name), 'wb')
		f.write(requests.get(img['src']).content)
		f.close()
	else:
		print('no have image for {0}'.format(name))



get_all_name_and_detail_link()

# driver.quit()