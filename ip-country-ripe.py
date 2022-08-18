#!/usr/bin/env python3
# coding: utf-8
# version: 0.4
from ipaddress import IPv4Address, IPv4Network, ip_address, summarize_address_range
import sys
import os
import json
import requests
from aggregate_prefixes import aggregate_prefixes

try:
  country_code = sys.argv[1].upper()
except:
  print('Usage: ', sys.argv[0], ' <two letters country code> ')
  exit()

networks = []
filepath = os.path.dirname(os.path.abspath(sys.argv[0]))
result = filepath + '/ip_' + country_code + '.lst'
url = 'https://stat.ripe.net/data/country-resource-list/data.json?resource='+country_code
ripe_ip = json.loads(requests.get(url).content)['data']['resources']['ipv4']
number_of_ips = 0

with open(result, 'w') as out_file:
    for record in ripe_ip:
#        try:
            if record.find('-') > -1:
                ips = record.split('-')
                ipaddr = list(summarize_address_range(IPv4Address(ips[0]),IPv4Address(ips[1])))
            else:
                ipaddr = [IPv4Network(record)]
            networks.extend(ipaddr)
#        except:
#            pass
    for line in list(aggregate_prefixes(networks)):
        number_of_ips += line.num_addresses
        print(str(line), file=out_file)
print('Total number of IPs is %d' % number_of_ips)