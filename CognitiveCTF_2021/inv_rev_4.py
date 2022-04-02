#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def decodeChar(data):
    return bin(data)[-1]

flag = ''

for n_file in range(5):
    filename = 'Item0' + str(5-n_file) + '_cp.bmp'
    with open(filename, 'rb') as f:
        data = f.read()[2019:2139] # 2019 + (40 + 10*8) = 2139

    data_e = b''
    for i in range(10):
        data_e += data[i*12:i*12+8]  # (5-1) + 8 = 12
        # print(i, data[i*12:i*12+8])
    
    for i in range(10):
        fragment = ''
        for j in range(8):
            fragment += decodeChar(data_e[i*8+7-j])
        flag += chr(int(fragment, 2))

print(flag)