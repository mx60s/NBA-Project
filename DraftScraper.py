from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
driver = webdriver.Chrome()

with open("./Desktop/draftFile.csv", "w+") as draftFile:
    for year in range(1960,2016):
        driver.implicitly_wait(10)
        driver.get(
            "https://stats.nba.com/draft/history/?Season=" + str(year) + "&CF=ROUND_NUMBER*L*3")
        table = driver.find_elements_by_xpath(
            '/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')
        for line in table:
            name = line.find_element_by_xpath(".//td[1]").text
            spot = line.find_element_by_xpath(".//td[7]").text
            draftFile.write(name + ", " + str(year) + ", " + spot + "\n")

draftFile.close()
driver.close()



