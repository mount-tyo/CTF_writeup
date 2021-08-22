#!/usr/bin/env python3
# -*- coding:utf-8 -*-

expected = [0xf4, 0xc0, 0x97, 0xf0, 0x77, 0x97, 0xc0, 0xe4, 0xf0, 0x77, 0xa4, 0xd0, 0xc5, 0x77, 0xf4, 0x86, 0xd0, 0xa5, 0x45, 0x96, 0x27, 0xb5, 0x77, 0xb4, 0xd1, 0xf1, 0xf1, 0xa5, 0xb4, 0xb4, 0xe0, 0xb4]

def switch(c, a, b):
    switched = c
    switched = switched[:a] + c[b] + switched[(a+1):]
    switched = switched[:b] + c[a] + switched[(b+1):]
    return switched

flag = ''
for e in expected:
    e_bin_str = bin(e)[2:]
    while len(e_bin_str) < 8:
        e_bin_str = '0' + e_bin_str
    e_bin_str = switch(e_bin_str, 6, 7)
    e_bin_str = switch(e_bin_str, 2, 5)
    e_bin_str = switch(e_bin_str, 3, 4)
    e_bin_str = switch(e_bin_str, 0, 1)
    e_bin_str = switch(e_bin_str, 4, 7)
    e_bin_str = switch(e_bin_str, 5, 6)
    e_bin_str = switch(e_bin_str, 0, 3)
    e_bin_str = switch(e_bin_str, 1, 2)
    # e_bin_str = switch(e_bin_str, 0, 3)
    # e_bin_str = switch(e_bin_str, 1, 2)
    flag += chr(int(e_bin_str,2))
print('picoCTF{' + flag + '}')