from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
driver = webdriver.Chrome()

#Get name from draftFile
statsFile = open("./Desktop/statsFile.csv", "w+")
linksFile = open("./Desktop/PlayerLinks.csv")
linksReader = csv.reader(linksFile)
draftFile = open("./Desktop/draftFile.csv")
draftReader = csv.reader(draftFile)

statsFile.write("Name, Position, Year, Spot, Games, WSp, VORP, PER, TS, BPM \n")

for draftRow in draftReader:
    name = draftRow[0]
    year = draftRow[1]
    spot = draftRow[2]
    link = "--"
    linksFile.seek(0)
    for linkRow in linksReader:
        if name == linkRow[0]:
            link = linkRow[1]
    ws = "0"
    vorp = "0"
    pos = "NA"
    per = "0"
    ts = "0"
    bpm = "0"
    games = "0"
    if link != "--":
        try:
            driver.get(link)
        except:
            print("EXCEPTION WAS THROWN")
            driver.close()
            driver = webdriver.Chrome()
            driver.get(link)

        tableHeader = driver.find_elements_by_xpath('//*[@id="advanced"]/thead/tr/th')

        index = "--"
        for cols in tableHeader:
            if cols.text == "WS/48":
                index = str(tableHeader.index(cols))
        if index != "--":
            ws = driver.find_element_by_xpath('//*[@id="advanced"]/tfoot/tr/td[' + index + ']').text

        index = "--"
        for cols in tableHeader:
            if cols.text == "VORP":
                index = str(tableHeader.index(cols))
        if index != "--":
            vorp = driver.find_element_by_xpath('//*[@id="advanced"]/tfoot/tr/td[' + index + ']').text

        index = "--"
        for cols in tableHeader:
            if cols.text == "PER":
                index = str(tableHeader.index(cols))
        if index != "--":
            per = driver.find_element_by_xpath('//*[@id="advanced"]/tfoot/tr/td[' + index + ']').text

        index = "--"
        for cols in tableHeader:
            if cols.text == "TS%":
                index = str(tableHeader.index(cols))
        if index != "--":
            ts = driver.find_element_by_xpath('//*[@id="advanced"]/tfoot/tr/td[' + index + ']').text

        index = "--"
        for cols in tableHeader:
            if cols.text == "BPM":
                index = str(tableHeader.index(cols))
        if index != "--":
            bpm = driver.find_element_by_xpath('//*[@id="advanced"]/tfoot/tr/td[' + index + ']').text

        index = "--"
        for cols in tableHeader:
            if cols.text == "G":
                index = str(tableHeader.index(cols))
        if index != "--":
            games = driver.find_element_by_xpath('//*[@id="advanced"]/tfoot/tr/td[' + index + ']').text

        ###########      find player Position #############
        table = driver.find_elements_by_xpath('//*[@id="totals"]/tbody/tr')
        posList = []
        for row in table:
            pos = row.find_element_by_xpath('.//td[4]').text
            posList.append(str(pos))
        playerPos = max(set(posList), key=posList.count)

        statsFile.write(name + ", " + playerPos + ", " + year + ", " + spot + ", " + games + ', ' + ws + ", " + vorp + ", " + per + ", " + ts + ", " + bpm + "\n")

statsFile.close()
driver.close()