
import os
import sys
import json
import requests
import re
import datetime


os.environ["http_proxy"]="http://###############"
os.environ["https_proxy"]="https://##############"
os.environ["no_proxy"]="###############"


cikti=""
ifade = "curl -v -H 'SEC:##################' -basic -k https://##########/api/reference_data/sets/######## | grep -Eo '(http|https)://[^/']+"
try:
        cikti = os.popen(ifade).read()
except:
        pass

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cikti)

for i in urls:
        print i


endpoint = "###########################"

header = {
    'Content-Type' : 'application/json'
}

data = {
    "token": "######################",
    #"urls": ["{0}".format(url)]
    "urls": urls
}

body = json.dumps(data)

response = requests.post(endpoint, headers=header, data=body, verify=False)

print response.text

dosya=open("/var/log/TI.log","a")
d_date = datetime.datetime.now()
dosya.write("\n")
reg_format_date = d_date.strftime("%Y-%m-%d %I:%M:%S %p")
dosya.write(response.text)
dosya.write("\t")
dosya.write(reg_format_date)
dosya.write("\n")
dosya.write("\n Data: \n")

for gur in urls:
        dosya.write("%s\n" % gur)

dosya.close()
