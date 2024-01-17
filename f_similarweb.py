import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv


options = uc.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Naveed Siddiqui\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2')
driver = uc.Chrome(options=options,use_subprocess=True)
wait = WebDriverWait(driver, 300)
driver.get("https://pro.similarweb.com/")
#------------ Maximize the Browser ---------------
driver.maximize_window()

def jswait():
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

jswait()

def single_row(crawling_link):

    single_row_dict = {}

    #------------ Redirection to Home Page for Next Record -----------------------
    home_logo = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'IconSidebarSection')]/span/div")))
    home_logo.click()
    time.sleep(2)
    jswait()
    #---------------- Searching Web Site in Main Sarch -----------------
    main_search = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains (@data-automation-icon-name, 'search')]/following::input")))
    main_search.click()
    jswait()
    main_search.send_keys(crawling_link)
    time.sleep(5)
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'input-container')]/div[2]")))
    main_search.send_keys(Keys.RETURN)
    #searched_website = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.AutoCompleteContainer div.ListItemWebsite"))).click()
    jswait()
    #----------------- Add Url Start of CSV -------------------
    single_row_dict.update(urls = crawling_link)
    
    # --------- Montly Visits ------------
    time.sleep(5)
    jswait()
    try:
        monthly_visits = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'MetricContainer')]//div[contains(text(), 'Monthly visits')]/../following::div")))
        #monthly_visits = driver.find_element(By.XPATH,"//div[contains(@class, 'MetricContainer')]//div[contains(text(), 'Monthly visits')]/../following::div")
        # print(monthly_visits.text)
        single_row_dict.update(monthly_visits = monthly_visits.text)
    except:
        single_row_dict.update(monthly_visits = "")
    
    try:
        # ---------- Navigate Demographics -------------
        domolink = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="react-app"]/div/div[5]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/div[2]/div/a[2]""")))
        domolink.click()
        time.sleep(5)

    #----------- Finding Male Distrubution ------------
    
        maledisper = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Male']/following::span")))
        single_row_dict.update(male_distribution = maledisper.text)
    except:
        single_row_dict.update(male_distribution = "")
    #----------- Finding Female Distrubution ------------
    try:
        femaledisper = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Female']/following::span")))
        single_row_dict.update(female_distribution = femaledisper.text)
        # time.sleep(2)
    except:
        single_row_dict.update(female_distribution = "")

    try:
        #------------- Age Distrubution --------------
        agedislabels = driver.find_elements(By.CSS_SELECTOR,"g.highcharts-data-labels.highcharts-column-series .highcharts-label")
        # ------ 18-24 ---------
        a18_24 = agedislabels[0].find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text
        single_row_dict.update(age18_24 = a18_24)
        # ------ 25-34 ---------
        a25_34 = agedislabels[1].find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text
        single_row_dict.update(age25_34 = a25_34)
        # ------ 35-44 ---------
        a35_44 = agedislabels[2].find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text
        single_row_dict.update(age35_44 = a35_44)
        # ------ 45-54 ---------
        a45_54 = agedislabels[3].find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text
        single_row_dict.update(age45_54 = a45_54)
        # ------ 55-64 ---------
        a55_64 = agedislabels[4].find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text
        single_row_dict.update(age55_64 = a55_64)
        # ------ 65+ ---------
        a65 = agedislabels[5].find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text
        single_row_dict.update(age65plus = a65)
    except:
        single_row_dict.update(age18_24 = "")
        single_row_dict.update(age25_34 = "")
        single_row_dict.update(age35_44 = "")
        single_row_dict.update(age45_54 = "")
        single_row_dict.update(age55_64 = "")
        single_row_dict.update(age65plus = "")
    # for agedislabel in agedislabels:
    #     print(agedislabel.find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text)

    # --------------- Navigate Geographics -----------------
    geobtn = driver.find_element(By.XPATH,"""//*[@id="react-app"]/div/div[5]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/div[2]/div/a[1]""")
    geobtn.click()
    time.sleep(5)
    
    try:
        #---------------- Searhing Canada in Search ---------------
        canadasearch = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".SearchInput-container .SearchInput")))
        # canadasearch = driver.find_element(By.CSS_SELECTOR,".SearchInput-container .SearchInput")
        canadasearch.click()
        canadasearch.send_keys("canada")
        time.sleep(1)
    
    #------------- Fetching Data from Canada Traffic Percentage If Present -----------------
    
        canadaper = driver.find_element(By.CSS_SELECTOR,"span.min-value")
        canadaper_existance = True
        # print(canadaper.text)
        single_row_dict.update(canada_traffic_share = canadaper.text)
    except:
        canadaper_existance = False
        single_row_dict.update(canada_traffic_share = "")
    return single_row_dict



#==================== Main Part of Program =========================
#===================================================================
#----------- List that Collect Dictionaries -----------
wrapper_list = []
i = 1
#-------- Reading Input from CSV ------------
with open('similarweb/input_data.csv') as file:
    reader = csv.reader(file)
    for crawling_link in reader:
        single_entry_dict = single_row(crawling_link[0].lower())
        wrapper_list.append(single_entry_dict)
        print(i)
        print(single_entry_dict)
        i = i + 1



# -------------- CSV File Writing --------------
with open('similarweb/scraped_data.csv', mode='w', newline='') as newfile:
    fieldnames = wrapper_list[0].keys()
    csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for row in wrapper_list:
        csv_writer.writerow(row)
newfile.close()

time.sleep(2)