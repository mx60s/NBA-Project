from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import copy
import os

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

# Get name from draftFile
statsFile = open("statsFile.csv", "w+")
linksFile = open("PlayerLinks.csv")
linksReader = csv.reader(linksFile)
#draftFile = open("./Desktop/draftFile.csv")
#draftReader = csv.reader(draftFile)

# lol
default_fields = dict()

"""
Get the fields
"""
link0 = "https://www.basketball-reference.com/players/a/abdulka01.html"
try:
    driver.get(link0)
except:
    print("EXCEPTION WAS THROWN")
    driver.close()
    driver = webdriver.Chrome()
    driver.get(link0)

perGameCol = driver.find_element_by_xpath('//table[@id="per_game"]/thead/tr')
advancedCol = driver.find_element_by_xpath('//table[@id="advanced"]/thead/tr')
tables = [perGameCol, advancedCol]

for table in tables:
    for col in table.find_elements_by_xpath(".//th"):
        label = col.get_attribute('data-stat')
        default_fields[label] = 0

default_fields["name"] = "NA"

if os.stat("statsFile.csv").st_size == 0:
    csv_header = ""
    for field in default_fields.keys():
        csv_header += field + ", "

    statsFile.write(csv_header + "\n")


"""
Iterate through players and collect values
"""
try:
    for player, link in linksReader:
        if player == "Warren Jabali":
            break
        try:
            driver.get(link)
        except:
            print("EXCEPTION WAS THROWN")
            driver.close()
            driver = webdriver.Chrome()
            driver.get(link)
        try:
            perGame = driver.find_element_by_xpath('//table[@id="per_game"]/tbody')
            advanced = driver.find_element_by_xpath(
                '//table[@id="advanced"]/tbody')

            pg_years = perGame.find_elements_by_xpath(".//tr")
            a_years = advanced.find_elements_by_xpath(".//tr")

            # for each year a player is active, get row data for that year from both tables
            for i in range(len(pg_years)):
                # start off with default fields
                playerData = copy.deepcopy(default_fields)
                try:
                    playerData["season"] = pg_years[i].find_element_by_xpath(
                        ".//th").find_element_by_xpath(".//a").text
                except:
                    continue

                for table in [pg_years, a_years]:
                    for col in table[i].find_elements_by_xpath(".//td"):
                        label = col.get_attribute('data-stat')
                        if not label:
                            continue
                        try:
                            if col.find_element_by_xpath(".//a").text:
                                playerData[label] = col.find_element_by_xpath(".//a").text
                        except:
                            if col.text:
                                playerData[label] = col.text

                playerData["name"] = player

                csv_line = ""
                for val in playerData.values():
                    csv_line += str(val) + ", "
                print(csv_line)
                statsFile.write(csv_line + "\n")
        except:
            continue
    statsFile.close()
    driver.close()

except Exception as e:
    print(e)
    statsFile.close()
    driver.close()
