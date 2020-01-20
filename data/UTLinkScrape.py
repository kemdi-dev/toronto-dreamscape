from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

linksFileName = "UTProjectLinks.txt"

def getBuildingLinks():
   driver = webdriver.Chrome()
   
   driver.get('http://urbantoronto.ca/database/')
   html = driver.page_source
   soup = BeautifulSoup(html,"html.parser")
   links = soup.findAll('a', attrs={'href': re.compile("^//urbantoronto.ca/database/projects")})

   with open(linksFileName, "w") as f:
       for tag in links :
           f.write(tag.get('href').encode('utf-8') + '\n')
           print (tag.get('href'))
       

getBuildingLinks();
    
