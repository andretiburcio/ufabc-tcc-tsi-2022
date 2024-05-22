import requests
from nssdca_list import url_spacecraft_id

url_base = "https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id="
output_finename = "detailedNSSDCA_list.csv"

x = 1

with open(output_finename,'w') as file:
        file.write("num;code;url;status_code;launch_date;launch_vehicle;launch_site;")
        file.write('\n')

for i in url_spacecraft_id:
    url = url_base + i
    r = requests.get(url)

    launch_date_start = r.text.index("Launch Date:")
    launch_date = r.text[launch_date_start+22:launch_date_start+32:]

    launch_vehicle_start = r.text.index("Vehicle:")
    launch_vehicle = r.text[launch_vehicle_start+18:launch_vehicle_start+38:]

    launch_site_start = r.text.index("Site:")
    launch_site = r.text[launch_site_start+15:launch_site_start+50:]

    print(x)

    with open(output_finename,'a') as file:
        file.write(str(x)+';'+i+';'+url+';'+str(r.status_code)+";"+launch_date+";"+launch_vehicle+";"+launch_site+';')
        file.write('\n') 
    x=x+1

    #TO DO: INSERIR O NOME DO SATÉLITE

