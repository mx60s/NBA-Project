from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import string
driver = webdriver.Chrome()

with open("./Desktop/PlayerLinks.csv", "w+") as file:
    for char in string.ascii_lowercase:
        driver.get("https://www.basketball-reference.com/players/" + char)

        #if table needs to be expanded, find element and clicks on it
        exists = True
        try:
            driver.find_element_by_id("players_control")
        except:
            exists = False
        if exists == True:
            driver.find_element_by_id("players_control").click()

        playerTable = driver.find_elements_by_xpath('//*[@id="players"]/tbody/tr')
        for line in playerTable:
            name = line.find_element_by_xpath(".//th").text
            nameFix = name.replace("*", "")
            link = line.find_element_by_css_selector('a').get_attribute('href')
            file.write(nameFix + ", " + link + "\n")
file.close()
driver.close()
