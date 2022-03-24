#!/usr/bin/env python3
# coding: utf-8
import requests
import sys
import subprocess
import re
from aggregate_prefixes import aggregate_prefixes

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://ftp.ripe.net/ripe/asnames/asn.txt'
networks = []
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})')

try:
  country_code = sys.argv[1].upper()
except:
  print('Usage: ', sys.argv[0], ' <two letters country code> ')
  exit()

result = 'ip_'+country_code+'.lst'

response = requests.get(url, headers=headers).text.split('\n')
asn = [ t.split(' ')[0] for t in response if t.split(' ')[-1] == country_code]
with open(result, "w") as out_file:
    for i in range(0, len(asn), 50):
        output = subprocess.check_output('/usr/bin/bgpq3 -3A AS'+' AS'.join(asn[i:i + 50]), shell=True, text=True)
        try:
           networks.extend(re.findall(pattern,output))
        except:
           pass
        print(len(networks))
    for line in list(aggregate_prefixes(networks)):
        print(str(line), file=out_file)
