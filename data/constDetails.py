import urllib2
from bs4 import BeautifulSoup
import time
import os.path
import csv

save_path ='/Users/kemdi/Desktop/assignment4' #change this path to a folder in your computer
fileName = "constructionDets.csv"
path_address = os.path.join(save_path, fileName)

def makeHeader():
    f = open(path_address, 'ab')
    header = ['Title', 'Address', 'Category', 'Status', 'Completion Date', 'Storeys', 'Height in ft']
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(header)
    f.close()

def scrape():
    filepath = '/Users/kemdi/Downloads/UTProjectLinks.txt'
    with open(filepath, "r") as fp:
        with open(path_address,'wb') as found:
            writer = csv.writer(found)
            print ('Results file created')
            writer.writerow(['Title', 'Address', 'Category', 'Status', 'Completion Date', 'Storeys', 'Height in ft'])
            #print(fp.readline())
            for line in fp:
                newlines = line.rstrip('\n')
                try:
                    page = urllib2.urlopen(newlines)
                except urllib2.HTTPError as err: #this filters out all the dead links
                    if err.code == 404:
                        print ("Not Found")
                        #rows = ['none', 'none', 'none', 'none', 'none', 'none']
                        #writer.writerow(rows)
                soup = BeautifulSoup(page, "html.parser")
                
                coltitle = soup.find('h1', attrs={'class':'title'})
                if (coltitle is not None):
                    forTitle = coltitle.text.encode('utf-8') #this takes care of the special characters
                    title = forTitle
                elif (coltitle is None):
                    title = "unknown"
                else:
                    title = coltitle.text
                
                col1 = soup.find('div', attrs={'class':'project-address odd'})
                if (col1 is not None):
                    findAddress = col1.text.encode('utf-8') #this takes care of the special characters
                    address = findAddress.replace("Address: ", "")
                elif (col1 is None):
                    address = "unknown"
                else:
                    address = col1.text.replace("Address: ", "")

                col2 = soup.find('div', attrs={'class':'project-category odd'})
                if (col2 is None):
                    col2 = soup.find('div', attrs={'class':'project-category even'})
                    if (col2 is not None):
                        category = col2.text.replace(col2.label.text, "")
                    else:
                        category = "unknown"
                else:
                    category = col2.text.replace(col2.label.text, "")
                
                col3 = soup.find('div', attrs={'class':'project-status even'})
                if (col3 is None):
                    col3 = soup.find('div', attrs={'class':'project-status odd'})
                    if (col3 is not None):
                        status = col3.text.replace(col3.label.text, "")
                    else:
                        status = "unknown"
                else:
                    status = col3.text.replace(col3.label.text, "")

                col4 = soup.find('div', attrs={'class':'project-completion odd'})
                if (col4 is None):
                    col4 = soup.find('div', attrs={'class':'project-completion even'})
                    if (col4 is not None):
                        compDate = str(col4.text.replace(col4.label.text, ""))
                        completion = int(filter(str.isdigit, compDate))
                    else:
                        completion = "0"
                else:
                    compDate = str(col4.text.replace(col4.label.text, ""))
                    completion = int(filter(str.isdigit, compDate))
                
                col5 = soup.find('div', attrs={'class':'project-storeys odd'})
                if (col5 is None):
                    col5 = soup.find('div', attrs={'class':'project-storeys even'})
                    if (col5 is not None):
                        forStoreys = col5.text.replace(col5.label.text, "")
                        storeys = forStoreys.split(', ', 1)[0]
                    else:
                        storeys = "0"
                else:
                    forStoreys = col5.text.replace(col5.label.text, "")
                    storeys = forStoreys.split(', ', 1)[0]

                col6 = soup.find('div', attrs={'class':'project-height even'})
                if (col6 is not None):
                    height = col6.text.replace(col6.label.text, "")
                    if (col6.label is not None):
                        for r in (("        ", ""), ("      ", ""), ('\n', ""), (" ft", "")):
                            forHeight = height.replace(*r)
                            height = forHeight.split(', ', 1)[0] #reads only the first height
                    else:
                        height = "0"
                else:
                    height = "0"
                if (title != "unknown"):
                    rows = [title, address, category, status, completion, storeys, height]
                    writer.writerow(rows)
                    print (rows)

#website_allData()
scrape()
