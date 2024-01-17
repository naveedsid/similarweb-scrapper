import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv

options = uc.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Naveed Siddiqui\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver = uc.Chrome(options=options,use_subprocess=True)

def single_row(crawl_link):
    single_row_dict = {}
    driver.get(crawl_link)
    #------------ Maximize the Browser ---------------
    driver.maximize_window()
    #------ Create Wait Driver ----------
    wait = WebDriverWait(driver, 300)
    # ---------- Wait Until Javascript Loads Properly -----------
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    # --------- Montly Visits ------------
    monthly_visits = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "MetricValue-ckkXpQ")))
    print(monthly_visits.text)
    single_row_dict.update(monthly_visits = monthly_visits.text)

    # ---------- Navigate Demographics -------------
    domolink = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="react-app"]/div/div[5]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/div[2]/div/a[2]""")))
    domolink.click()
    time.sleep(2)

    #----------- Finding Male Distrubution ------------
    maledisper = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Male']/following::span")))
    single_row_dict.update(male_distribution = maledisper.text)
    
    #----------- Finding Female Distrubution ------------
    femaledisper = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Female']/following::span")))
    single_row_dict.update(female_distribution = femaledisper.text)
    # time.sleep(2)

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

    # for agedislabel in agedislabels:
    #     print(agedislabel.find_element(By.CSS_SELECTOR,"tspan.highcharts-text-outline").text)

    # --------------- Navigate Geographics -----------------
    geobtn = driver.find_element(By.XPATH,"""//*[@id="react-app"]/div/div[5]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/a[3]/div[2]/div/a[1]""")
    geobtn.click()
    time.sleep(2)
    
    #---------------- Searhing Canada in Search ---------------
    canadasearch = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".SearchInput-container .SearchInput")))
    # canadasearch = driver.find_element(By.CSS_SELECTOR,".SearchInput-container .SearchInput")
    canadasearch.click()
    canadasearch.send_keys("canada")
    
    #------------- Fetching Data from Canada Traffic Percentage If Present -----------------
    try:
        canadaper = driver.find_element(By.CSS_SELECTOR,"span.min-value")
        canadaper_existance = True
        # print(canadaper.text)
        single_row_dict.update(canada_traffic_share = canadaper.text)
    except:
        canadaper_existance = False
        single_row_dict.update(canada_traffic_share = "")
    return single_row_dict


crawling_links = [
                  "https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=collider.com",
                  "https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=cochraneeagle.ca",
                  "https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=coastreporter.net",
                  "https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=classicalfm.ca",
                  "https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=butwhytho.net",
                  "https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=avclub.com"
                  ]

#----------- List that Collect Dictionaries -----------
wrapper_list = []

for crawling_link in crawling_links:    
    single_entry_dict = single_row(crawling_link)
    wrapper_list.append(single_entry_dict)
    print(wrapper_list)


# -------------- CSV File Writing --------------
with open('data.csv', mode='w', newline='') as newfile:
    fieldnames = wrapper_list[0].keys()
    csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for row in wrapper_list:
        csv_writer.writerow(row)
newfile.close()

















    
    # element_text = element.get_attribute("innerHTML")
# feprcss = ".LegendContainer-rtlIb.kGbbcs span:nth-child(2)"
# fperele = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, feprcss)))
# fperelehtml = fperele.get_attribute("innerHTML")
# print(fperelehtml)



# driver.header_overrides = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

# ------ Demographics link ----------
# tclass = "sc-cTbcWX iZEffJ"
# delement = wait.until(EC.presence_of_element_located((By.CLASS_NAME, tclass)))
# delement.click()

time.sleep(5)

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text")))