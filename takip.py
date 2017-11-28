import os
import sys
import json
import requests
import re
import datetime
import ast
import time
import datetime

#os.environ["http_proxy"]="################"
#os.environ["https_proxy"]="###################"
#os.environ["no_proxy"]="#################"


def icerikBizimMi(response):

        if response == "Kapalı":
                return False

        cevap = response.text

        if cevap.find("##############################") != -1:
                return True
        else:
                return False


def siteDurumGetir(url):
        try:
                r = requests.get("http://" + url.rstrip(), verify=False)
                return r
        except:
                return "Kapalı"


cikti=""
ifade = "curl -v -H 'SEC:#####################' -basic -k https://##############/api/reference_data/sets/##############"

try:
        cikti = os.popen(ifade).read()
except:
        pass


def YirmiDortCheck(ls_time):
        now = int(time.time())
        n_ls_time = ls_time / 1000
        diff = now - int(n_ls_time)
        if diff > 86400:
                return True
        else:
                return False


yapi=ast.literal_eval(cikti)

dosya=open("/var/log/#############.log","a")
adet=0

dosya.write("Kontrol basliyor\n")
d_date = datetime.datetime.now()
dosya.write(d_date.strftime("%Y-%m-%d %I:%M:%S %p"))
dosya.write("\n")

for i in yapi["data"]:
        icerikBizim = icerikBizimMi(siteDurumGetir(i["value"]))
        if icerikBizim:
                print i["value"]+",Aktif"
                dosya.write(i["value"])
                dosya.write(",Aktif")
                dosya.write(",")
                dosya.write(str(i["last_seen"]))
                if YirmiDortCheck(i["last_seen"]):
                        dosya.write(",*** 24 saat ***")

                dosya.write("\n")
                adet += 1
        else:
                print i["value"]+",Pasif"
                dosya.write(i["value"])
                dosya.write(",Pasif\n")

dosya.write("\n\nAktif sayisi: ")
dosya.write(str(adet))
dosya.write("\n####################\n\n")
dosya.close()

