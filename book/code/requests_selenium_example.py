import  requests
url = 'https://www.youtube.com/'
response = requests.get(url)
print(response.content)

# from selenium import  webdriver
# options = webdriver.ChromeOptions()
# options.headless  = False
# driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', 
# 						options=options)
# driver.get(url)
# print(driver.page_source)



