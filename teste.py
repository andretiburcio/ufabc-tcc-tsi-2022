
#import urllib.request
#contents = urllib.request.urlopen("https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2019-074A").read()

import requests
import numpy as np
import csv

url_base = "https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id="
url_spacecraft_id = [
    '2019-029L',
'2019-029B',
'2019-029C']
x = 1


with open('data.csv', 'w', newline='') as f:
    write = csv.writer(f)
    for i in url_spacecraft_id:
        url = url_base + i
        r = requests.get(url)

        launch_date_start = r.text.index("Launch Date:")
        launch_date = r.text[launch_date_start+22:launch_date_start+32:]

        launch_vehicle_start = r.text.index("Vehicle:")
        launch_vehicle = r.text[launch_vehicle_start+18:launch_vehicle_start+38:]

        launch_site_start = r.text.index("Site:")
        launch_site = r.text[launch_site_start+15:launch_site_start+50:]

        print(x,i,url,';',r.status_code,";",launch_date,";", launch_vehicle,";",launch_site)
        #np.savetxt('data.csv', (x, i, url,r.status_code,launch_date,launch_vehicle), delimiter=',')
        data ='x,i,url,";",r.status_code,";",launch_date,";", launch_vehicle,";",launch_site'

        write.writerow(launch_site)
        x=x+1

        #TO DO: INSERIR O NOME DO SATÉLITE



