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
filepath = os.path.dirname(sys.argv[0])
asndb = pyasn.pyasn(filepath+'/ipasn.lst')
asnf = filepath + '/asn.txt'
result = filepath + '/ip_' + country_code + '.lst'

with open(result, 'w') as out_file, open(asnf, 'r') as asn_file:
    asn = [ t.split(' ')[0] for t in asn_file if t.split(' ')[-1][:2] == country_code]
    for i in asn:
        output = asndb.get_as_prefixes(i)
        try:
            networks.extend(list(output))
        except:
            pass
    for line in list(aggregate_prefixes(networks)):
        print(str(line), file=out_file)
