import csv
import time
from  geopy.geocoders import Nominatim

#geolocator = Nominatim()
save_path ='/Users/vivie/Desktop/data vis/project_4/demolDets2015.csv'

with open('OGdemolDets2015.csv') as csvDataFile:
    reader = csv.reader(csvDataFile)
    next(reader, None)
    with open(save_path,'ab') as found:
        writer = csv.writer(found)
        writer.writerow(['Address', 'Latitude', 'Longitude', 'Status', 'Application Date', 'Completion Date', 'Description', 'Current Use'])

        for row in reader:
            geolocator = Nominatim()
            address = row[0].strip()
            #quiry for lat and lng and remember to sleep(1)
            fullAddress = address + ", Toronto Canada"
            loc = geolocator.geocode(fullAddress)
            try:
                lat = loc.latitude
                lng = loc.longitude
                print(address)
            except:
                print("skipped error")
                next(reader, None)
            if lat < 43.59367014 or lat > 43.79663682:
                print("skipped off lat")
                next(reader, None)
            if lng < -79.594317 or lng > -79.1843517:
                print("skipped off lng")
                next(reader, None)
                             
            stat = row[1]
            appDate = row[2]
            compDate = row[3]
            des = row[4]
            curr = row[5]

            line = [address, lat, lng, stat, appDate, compDate, des, curr]
            writer.writerow(line)
            
            time.sleep(1)

            
