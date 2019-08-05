from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

# create option object
options = Options()
options.headless = True

# specify execution path
# chrome_driver_path = r'C:\chromedriver_win32\chromedriver.exe'
chrome_driver_path = r'/Users/tanpv/chromedriver'

# create driver
driver = webdriver.Chrome(chrome_driver_path, options=options)

# try to get a url
url = 'https://www.google.com/search?source=hp&ei=95kmXZ-VF4j48gX8zJKwAw&q=selenium&oq=selenium&gs_l=psy-ab.3..0l10.42275.44835..45106...1.0..0.95.652.9......0....1..gws-wiz.....0..0i131.xjVRyx35-9Q'
driver.get(url)

# get html
soup = BeautifulSoup(driver.page_source,'lxml')
print(soup)

