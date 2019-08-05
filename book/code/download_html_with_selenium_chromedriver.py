# import webdriver
from selenium import webdriver

# create Chrome object
driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')

# access url
driver.get('https://www.nba.com/')

# access HTML content
print(driver.page_source)

# close browser
driver.close()