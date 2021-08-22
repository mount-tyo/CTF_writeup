#!/usr/bin/env python3
# -*- coding:utf-8 -*

from pprint import pprint

def pad8(b):
        while len(b) < 8:
            b = '0' + b
        return b

if __name__ == '__main__':
    # read enc_map
    enc_map = {}
    with open('map.txt', 'rb') as f:
        enc_data = f.readlines()
    for l in enc_data:
        line = l.decode().strip()
        enc_map[line.split(': ')[0]] = line.split(': ')[1]

    # decode
    with open('output', 'rb') as f:
        data = f.read()

    bin_str = ''
    for d in data:
        bin_str += pad8(bin(d)[2:])
    
    print('output bin: ' + str(bin_str))

    flag = ''
    
    b_search = ''
    for b in bin_str:
        b_search += b
        if b_search in enc_map.values():
            dec = [k for k, v in enc_map.items() if v == b_search][0]
            # print(dec)
            flag += dec
            b_search = ''
    print('flag: ' + flag)