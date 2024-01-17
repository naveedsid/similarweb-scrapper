# Scrapper for Similar Web
Make sure you have install python latest version on your pc, by typing "python --version" in CMD
Before you run the scirpt, you have to create an free account on similarweb and activate your free trail
 Open your CMD and run these commands to install the require libraries
"pip install undetected_chromedriver"
"pip install selenium"

#1 Create a folder named as "similarweb" put the script in that folder
#2 Create a CSV File and put the links in it (from you want data), named that file "input_data.csv"
Note: Feed 20 to 30 Links as per execution, because site has anti scrapping bots, that might block your account
#3  Rename your Google Chrome Profile link which you want to use, on Line No. 11 Like this
"C:\\Users\\Naveed Siddiqui\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2"
You can fetch your profile link by typing "chrome://version" in address bar, here you will find your profile address named as "Profile Path"
#4 After the execution of script a file will created named as "scraped_data" in same folder