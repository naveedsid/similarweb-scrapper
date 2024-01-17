# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time

# target_url = "https://www.youtube.com"
# time.sleep(5)
# driver.get("https://gmail.com")
# time.sleep(50)

# html = driver.page_source
# print(html)


# ---------- Working Version 1 --------
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--profile-directory=default')
# chrome_options.add_argument('--user-data-dir=C:\\Users\\Naveed Siddiqui\\AppData\\Local\\Google\\Chrome\\User Data')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://gmail.com")

# ---------- Working Version 2 --------
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.wait import WebDriverWait
options = uc.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Naveed Siddiqui\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver = uc.Chrome(options=options,use_subprocess=True)
driver.get('https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=iheartradio.ca')
time.sleep(15)



# ---------- Working Version 3 --------
# import undetected_chromedriver as uc
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument('--profile-directory=default')
# options.add_argument('--user-data-dir=C:\\Users\\Naveed Siddiqui\\AppData\\Local\\Google\\Chrome\\User Data\\')
# driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe",options=options)
# driver.get('https://google.com')