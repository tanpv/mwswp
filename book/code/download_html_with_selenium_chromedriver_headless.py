# import webdriver
from selenium import webdriver

# create option for headness mode
options = webdriver.ChromeOptions()
options.headless = True

# create Chrome object
driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe',
							options=options)

# access url
driver.get('https://www.nba.com/')

# access HTML content
print(driver.page_source)

# close browser
driver.close()