from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import string
import unidecode

driver = webdriver.Chrome()

with open("PlayerLinks.csv", "w+") as linkFile:
    for char in string.ascii_lowercase:
        driver.get("https://www.basketball-reference.com/players/" + char)

        playerTable = driver.find_elements_by_xpath('//*[@id="players"]/tbody/tr')
        for line in playerTable:
            if (line.get_attribute("class") != "thead"):
                name = line.find_element_by_xpath(".//th").text
                nameFix = unidecode.unidecode(name.replace("*", ""))
                link = line.find_element_by_css_selector('a').get_attribute('href')
                #print(nameFix)
                #print(link)
                linkFile.write(nameFix + ", " + link + "\n")

linkFile.close()
driver.close()




