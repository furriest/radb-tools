#!/usr/bin/env python3
# coding: utf-8
# version: 0.4
import sys
import os
import pyasn
from aggregate_prefixes import aggregate_prefixes

try:
  country_code = sys.argv[1].upper()
except:
  print('Usage: ', sys.argv[0], ' <two letters country code> ')
  exit()

networks = []
filepath = os.path.dirname(os.path.abspath(sys.argv[0]))
asndb = pyasn.pyasn(filepath+'/ipasn.lst')
asnfile = filepath + '/asn.txt'
result = filepath + '/ip_' + country_code + '.lst'
number_of_ips = 0

with open(result, 'w') as out_file, open(asnfile, 'r') as asn_file:
    asn_list = [ t.split(' ')[0] for t in asn_file if t.split(' ')[-1][:2] == country_code]
    for asn in asn_list:
        try:
            networks.extend(list(asndb.get_as_prefixes(asn)))
        except:
            pass
    for line in list(aggregate_prefixes(networks)):
        number_of_ips += line.num_addresses
        print(str(line), file=out_file)
print('Total number of IPs is %d' % number_of_ips)