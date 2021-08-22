with open("encoded.bmp", "rb") as f:
    f.seek(0x2d3)

    for j in range(100):
        if (j & 1) == 0:
            b = ""
            for k in range(8):
                data = f.read(1)
                b += str(int.from_bytes(data, 'big') & 1)
            c = int(b[::-1], 2)
            print(chr(c), end="")
        else:
            f.read(1)
    print()