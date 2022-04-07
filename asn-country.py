#!/usr/bin/env python3
# coding: utf-8
# version: 0.4
import sys
import os

try:
  country_code = sys.argv[1].upper()
except:
  print('Usage: ', sys.argv[0], ' <two letters country code> ')
  exit()

filepath = os.path.dirname(sys.argv[0])
result = filepath + '/asn_' + country_code + '.lst'
asnf = filepath + '/asn.txt'

with open(result, 'w') as out_file, open(asnf, 'r') as asn_file:
    asn = [ t.split(' ')[0] for t in asn_file if t.split(' ')[-1][:2] == country_code]
    for line in asn:
        print(str(line), file=out_file)
