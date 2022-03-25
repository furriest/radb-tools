#!/usr/bin/env python3
# coding: utf-8
# version: 0.3
import requests
import sys
import subprocess
import os
import pyasn
from aggregate_prefixes import aggregate_prefixes

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://ftp.ripe.net/ripe/asnames/asn.txt'
networks = []
filepath = os.path.dirname(sys.argv[0])
asndb = pyasn.pyasn(filepath+'/ipasn.lst')

try:
  country_code = sys.argv[1].upper()
except:
  print('Usage: ', sys.argv[0], ' <two letters country code> ')
  exit()

result = filepath + '/ip_' + country_code + '.lst'

response = requests.get(url, headers=headers).text.split('\n')
asn = [ t.split(' ')[0] for t in response if t.split(' ')[-1] == country_code]
with open(result, "w") as out_file:
    for i in range(0, len(asn), 1):
        output = asndb.get_as_prefixes(asn[i])
        try:
            networks.extend(list(output))
        except:
           pass
    for line in list(aggregate_prefixes(networks)):
        print(str(line), file=out_file)
