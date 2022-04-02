from Crypto.Cipher import AES
import os
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))


def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index(b'\n') + 1], s[s.index(b'\n')+1:]


def parse_header_ppm(f):
    data = f.read()

    header = b""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data


def abc_decrypt(ct):
    
    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) // BLOCK_SIZE)]
    iv = blocks[0]
    print(iv)
    decrypted_blks = []
    
    for i in range(len(blocks) - 1):
        prev_blk = int.from_bytes(blocks[i], 'big')
        curr_blk = int.from_bytes(blocks[i+1], 'big')
        
        n_curr_blk = (curr_blk - prev_blk) % UMAX
        decrypted_blks.append( n_curr_blk.to_bytes(16, 'big'))

    data = b"".join(decrypted_blks)
    
    return data

if __name__=="__main__":

    with open('body.enc.ppm', 'rb') as f:
        header, c_img = parse_header_ppm(f)
    
    data = abc_decrypt(c_img)

    with open('flag.ppm', 'wb') as fw:
        fw.write(header)
        fw.write(data)