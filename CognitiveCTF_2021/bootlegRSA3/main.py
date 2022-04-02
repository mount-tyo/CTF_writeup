from pwn import *
from egcd import egcd
from Crypto.Util.number import *
import sympy

def totient(n):
    factors = sympy.factorint(n)
    rst = 1
    for i,j in factors.items():
        rst *= (pow(i,j) - pow(i,j-1))
    return rst

def main():
    c = 1
    n = 1
    e = 1

    phi = totient(n)
    d = egcd(e, phi)[1]
    if d < 0:
        d += phi

    m = pow(c, d, n)
    print("Decrypted m = {}".format(m))
    print("FLAG is {}".format(long_to_bytes(m)))



if __name__ == "__main__":
    main()