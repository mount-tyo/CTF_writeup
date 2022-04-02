# open bmp file
with open("./encoded.bmp", "rb") as f:
    # 2000[byte] offset from the beginning
    f.seek(2000)

    # flag from 2000th byte to 400 bytes
    # [ 2000 bytes named A ] + [ 400 bytes named B ] + [ remaining data... ]
    # B is flag data
    for _ in range(50):
        a = ""
        for _ in range(8):
            # read 1[bit] ?
            data = f.read(1)
            # 
            a += str(int.from_bytes(data, 'big') & 1)
            # print(f"  a = {a}")
        b = int(a[::-1], 2) + 5
        print(chr(b), end="")
    print()

