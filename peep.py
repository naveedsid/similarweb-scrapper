# import asyncio
# from pyppeteer import launch

# async def main():
#     # Specify the path to your Chrome user profile directory
#     user_profile_directory = r"C:\Users\Naveed Siddiqui\AppData\Local\Google\Chrome\User Data\Default"

#     # Launch Chrome with the existing profile
#     browser = await launch(executablePath='chrome.exe', userDataDir=user_profile_directory, headless=True)
#     page = await browser.newPage()

#     # Perform scraping tasks
#     await page.goto('https://www.similarweb.com/target_page')
#     content = await page.content()

#     # Close the browser
#     await browser.close()

#     # Process the scraped content
#     # ...

# # Run the asyncio event loop
# asyncio.get_event_loop().run_until_complete(main())

import csv
# wrapper_list = [{'monthly_visits': '691,011', 'male_distribution': '66.25%', 'female_distribution': '33.75%', 'age18_24': '33.67%', 'age25_34': '33.36%', 'age35_44': '16.90%', 'age45_54': '8.54%', 'age55_64': '4.98%', 'age65plus': '2.55%', 'canada_traffic_share': ''}, {'monthly_visits': '11.93M', 'male_distribution': '62.06%', 'female_distribution': '37.94%', 'age18_24': '20.38%', 'age25_34': '29.58%', 'age35_44': '20.17%', 'age45_54': '14.14%', 'age55_64': '10.25%', 'age65plus': '5.47%', 'canada_traffic_share': '68.06%'}]

# with open('data.csv', mode='w', newline='') as newfile:
#     fieldnames = ["1","2","3"]
#     csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     # for row in wrapper_list:
#     #     csv_writer.writerow(row)
#     csv_writer.writerow({"1":"1c","2":"2c","3":"3c"})

# print(wrapper_list[0].keys())
# ofile.close()



with open('similarweb/working.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])







# crawling_links = [
#                   #"https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/3m?webSource=Total&key=collider.com",
#                   "http://cochraneeagle.ca",
#                   "https://www.coastreporter.net/company/applicants",
#                   "www.classicalfm.ca/new_links",
#                   "butwhytho.net/students/applicant",
#                   "avclub.com"
#                   ]

        #------------ Link Parsing ---------------
        # parsed_link = urllib.parse.urlparse(crawling_link[1])
        # if parsed_link.scheme == '':
        #     domain = parsed_link.path  
        # else:
        #     domain = parsed_link.netloc
        # domain = domain.strip("www.").split('/')[0]
        # domain = domain.lower()



    
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

# time.sleep(2)

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text")))