import urllib2
from bs4 import BeautifulSoup
import time
import os.path
import csv

save_path ='/Users/kemdi/Desktop/assignment4' #change this path to a folder in your computer
fileName = "demolDets2015.csv"
path_address = os.path.join(save_path, fileName)

def makeHeader():
    f = open(path_address, 'ab')
    header = ['Address', 'Status', 'Application Date', 'Completion Date', 'Description', 'Current Use']
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(header)
    f.close()

def scrape():
    filepath = '/Users/kemdi/Downloads/clearedpermits2015.csv'
    with open(filepath, 'r') as csvfile:
        #reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        reader = csv.DictReader(csvfile)
        with open(path_address,'wb') as found:
            writer = csv.writer(found)
            print ('Results file created')
            writer.writerow(['Address', 'Status', 'Application Date', 'Completion Date', 'Description', 'Current Use'])
            for row in reader:
                allStatus = row["WORK"]
                allClosed = row["STATUS"]
                
                if (allStatus == "Demolition" and allClosed == "Closed"):
                    use = row["CURRENT_USE"]
                    if (use != "Vacant" and use != "Garage"):
                        if "Sfd" not in use:
                            if "Single-Family" not in use:
                                if "Single Family" not in use:
                                    add1 = row["STREET_NUM"]
                                    add2 = row["STREET_NAME"]
                                    add3 = row["STREET_TYPE"]
                                    add4 = row["STREET_DIRECTION"]
                                    forAddress = [add1, add2, add3, add4]
                                    address = ' '.join(forAddress)
                                    completion = row["COMPLETED_DATE"]
                                    appDate = row["APPLICATION_DATE"]
                                    closed = allClosed
                                    status = allStatus
                                    description = row["DESCRIPTION"]
                                    use = use
                                    rows = [address, status, appDate, completion, description, use]
                                    writer.writerow(rows)
                                    print(row)
                                    time.sleep(1)

#website_allData()
scrape()
